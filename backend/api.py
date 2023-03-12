from flask import Flask, request
from helperFunctions import *

app = Flask(__name__)


# TODO : ADD USER AUTH
@app.route("/login", methods=["POST"])
def login():
    expectedData = ["username", "hashedPassword"]
    receivedData = request.get_json()

    try:
        receivedData = extract_required_data(receivedData, expectedData)
    except:
        return server_response(status=500)
    else:
        userSessionID = ""
        return server_response(status=200, json={"userSessionID": userSessionID})


@app.route("/markAttendance", methods=["POST"])
def markAttendance():
    expectedData = ["studentID", "answer", "questionID", "lectureSessionID"]
    receivedData = request.get_json()

    try:
        receivedData = extract_required_data(receivedData, expectedData)
    except:
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
def startSession():
    expectedData = ["lecturerID", "sessionTime", "sessionDate", "subjectID"]
    receivedData = request.get_json()

    try:
        receivedData = extract_required_data(receivedData, expectedData)
    except:
        return server_response(status=500)

    sessionID = gen_code()
    columns = list(receivedData.keys())
    columns.insert(0, "sessionID")

    values = list(receivedData.values())
    values.insert(0, sessionID)

    try:
        insert_into_table("lectureSessions", columns, values)
    except:
        return server_response(status=500)
    else:
        return server_response(status=200, json={"lectureSessionID": sessionID})


@app.route("/", methods=["GET"])
def testConnection():
    return server_response(status=200)


@app.route("/register", methods=["POST"])
def register():
    expectedData = ["firstName", "lastName", "subjectIDs", "hashedPass"]
    receivedData = request.get_json()

    entityName = receivedData["entityName"]

    try:
        receivedData = extract_required_data(receivedData, expectedData)
    except:
        return server_response(status=500)

    entityID = gen_code()
    columns = list(receivedData.keys())
    values = list(receivedData.values())

    try:
        if entityName == "lecturer":
            columns.insert(0, "lecturerID")
            values.insert(0, entityID)
            insert_into_table("lecturers", columns, values)
        elif entityName == "student":
            columns.insert(0, "studentID")
            values.insert(0, entityID)
            insert_into_table("students", columns, values)
        else:
            raise Exception("Invalid Entity Name")
    except:
        return server_response(status=500)
    else:
        return server_response(status=200)


if __name__ == "__main__":
    app.run(port=3669)
