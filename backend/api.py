from flask import Flask, request
from helperFunctions import *
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

# TODO : ADD USER AUTH
@app.route("/login", methods=["POST"])
@cross_origin()
def login():
    expectedData = [
        "email",
        "hashedPassword",
    ]
    receivedData = request.get_json()

    try:
        userType = receivedData["userType"]
        receivedData = extract_required_data(receivedData, expectedData)
    except:
        print("[SERVER] - Required Data Could Not Be Extracted ")
        return server_response(status=500)
    else:
        userSessionID = ""
        return server_response(status=200, json={"userSessionID": userSessionID})

    # TODO
    # get user row from table
    # check if hashedpass an db hashpass is same
    # generate userSesssion code and save to db
    # return user session code


@app.route("/markAttendance", methods=["POST"])
@cross_origin()
def markAttendance():
    expectedData = ["studentID", "answer", "questionID", "lectureSessionID"]
    receivedData = request.get_json()

    try:
        receivedData = extract_required_data(receivedData, expectedData)
    except:
        print("[SERVER] - Required Data Could Not Be Extracted ")
        return server_response(status=500)

    query = 'SELECT * FROM Lecturer WHERE EXISTS(SELECT * From Lecturer WHERE lecturerID LIKE "%s")'

    try:
        if not check_for_item_in_table(
            "students", "studentID", receivedData["studentID"]
        ):
            raise Exception("StudentID not registered")
    except:
        return server_response(status=500)

    # TODO: check if sessionID is valid and studentID is valid
    return server_response(status=200, json=receivedData)


@app.route("/startSession", methods=["POST"])
@cross_origin()
def startSession():
    expectedData = [
        "lecturerID",
        "sessionTime",
        "sessionDate",
        "subjectID",
        "questionSource",
    ]
    receivedData = request.get_json()

    try:
        receivedData = extract_required_data(receivedData, expectedData)
    except:
        print("[SERVER] - Required Data Could Not Be Extracted ")
        return server_response(status=500)

    sessionID = gen_code()
    columns = list(receivedData.keys())
    columns.insert(0, "sessionID")

    values = list(receivedData.values())
    values.insert(0, sessionID)

    try:
        insert_into_table("lecturesessions", columns, values)
    except:
        print("[SERVER] - Row Could Not Be Inserted Into Table")
        return server_response(status=500)
    else:
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
        print("[SERVER] - Required Data Could Not Be Extracted ")
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
    else:
        return server_response(status=200)


if __name__ == "__main__":
    app.run(port=5000)
