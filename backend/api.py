from flask import Flask, request
from helperFunctions import *
from flask_cors import CORS, cross_origin
from datetime import datetime

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

# TODO : ADD USER AUTH
@app.route("/login", methods=["POST"])
@cross_origin()
def login():
    receivedData = request.get_json()

    try:
        userType = receivedData["userType"]
        email = receivedData["email"]
        hashedPass = receivedData["hashedPass"]
    except:
        print("[SERVER] - Required Data Could Not Be Extracted from POST data!")
        return server_response(status=500)

    # get user row from table
    try:
        if userType == "student":
            userRow = get_row_from_table("students", "email", email)
        elif userType == "lecturer":
            userRow = get_row_from_table("lecturers", "email", email)

        if len(userRow) == 0:
            print("[SERVER] - User Not Found")
        elif len(userRow) > 1:
            print("[SERVER] - Multple Users Found in the db")
    except:
        # return server_response(status=500)
        return {"message": email}, 500

    dbHashedPass = userRow[0][4]

    # check password

    if hashedPass != dbHashedPass:
        print("[SERVER] - Invalid Password")
        return {"message": hashedPass}, 500

    # save user session code in db and return
    userSessionCode = gen_code(10)
    expiry = datetime_to_string(time_plus_hours(datetime.now(), 1))
    try:
        columns = ["userSessionID", "expiry"]
        values = [userSessionCode, expiry]
        insert_into_table("usersessions", columns, values)
    except:
        print("[SERVER] - Problem Saving session key to db")
        return server_response(status=500)

    # return server_response(status=200, json={"userSessionKey": userSessionCode})
    return {"userSessionKey": userSessionCode}, 200


@app.route("/markAttendance", methods=["POST"])
@cross_origin()
def markAttendance():
    receivedData = request.get_json()
    expectedData = [
        "email",
        "lectureSessionID",
    ]
    receivedData = request.get_json()

    try:
        lectureSessionID = receivedData["lectureSessionID"]
        userSessionID = receivedData["userSessionID"]
        receivedData = extract_required_data(receivedData, expectedData)
    except:
        print("[SERVER] - Required Data Could Not Be Extracted from POST data!")
        return server_response(status=500)

    # check if usersessionID is valid
    if not user_session_validataion(userSessionID):
        print("[SERVER] - User is not Authenticated")
        return server_response(status=500)

    # check is lecturesessionID is valid
    if not lectureSesssion_validation(lectureSessionID):
        print("[SERVER] - Invalid LecutreSession")
        return server_response(status=500)

    # mark attendance in table
    try:
        columns = list(receivedData.keys())
        values = list(receivedData.values())
        insert_into_table("attendance", columns, values)
    except:
        print("[SERVER] - Row Could Not Be Inserted Into Table")
        return server_response(status=500)

    return server_response(status=200)


@app.route("/startSession", methods=["POST"])
@cross_origin()
def startSession():
    expectedData = [
        "lecturerID",
        "sessionStart",
        "sessionEnd",
        "subjectID",
        "questionSource",
    ]
    receivedData = request.get_json()

    try:
        userSessionID = receivedData["userSessionID"]
        receivedData = extract_required_data(receivedData, expectedData)
    except:
        print("[SERVER] - Required Data Could Not Be Extracted from POST data!")
        return server_response(status=500)

    if not user_session_validataion(userSessionID):
        print("[SERVER] - User is not Authenticated")
        return server_response(status=500)

    sessionID = gen_code(5)
    columns = list(receivedData.keys())
    columns.insert(0, "sessionID")

    values = list(receivedData.values())
    values.insert(0, sessionID)

    try:
        insert_into_table("lecturesessions", columns, values)
    except:
        print("[SERVER] - Row Could Not Be Inserted Into Table")
        return server_response(status=500)

    return server_response(status=200, json={"lectureSessionID": sessionID})


@app.route("/", methods=["GET"])
@cross_origin()
def testConnection():
    return server_response(status=200)


@app.route("/register", methods=["POST"])
@cross_origin()
def register():
    expectedData = [
        "email",
        "firstName",
        "lastName",
        "subjectIDs",
        "hashedPass",
    ]
    receivedData = request.get_json()

    try:
        userType = receivedData["userType"]
        receivedData = extract_required_data(receivedData, expectedData)
    except:
        print("[SERVER] - Required Data Could Not Be Extracted from POST data!")
        return server_response(status=500)

    columns = list(receivedData.keys())
    values = list(receivedData.values())

    try:
        if userType == "lecturer":
            insert_into_table("lecturers", columns, values)
        elif userType == "student":
            insert_into_table("students", columns, values)
        else:
            raise Exception("InvalidUserType")
    except:
        return server_response(status=500)

    return server_response(status=200)


@app.route("/getQuestion", methods=["POST"])
@cross_origin()
def get_question():
    receivedData = request.get_json()

    try:
        lectureSessionID = receivedData["lectureSessionID"]
        userSessionID = receivedData["userSessionID"]
    except:
        print("[SERVER] - Required Data Could Not Be Extracted from POST data!")
        return server_response(status=500)

    if not user_session_validataion(userSessionID):
        print("[SERVER] - User is not Authenticated")
        return server_response(status=500)

    try:
        result = get_random_question_from_db(lectureSessionID)
    except:
        print("[SERVER] - Questions are not available yet. Please try Later")
        return server_response(status=500)

    result = result[0]
    return server_response(
        status=200,
        json={
            "questionID": result[0],
            "question": result[1],
            "answer": result[2],
            "wronganswer": result[3],
        },
    )


if __name__ == "__main__":
    app.run(port=5000)
