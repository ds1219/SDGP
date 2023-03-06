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

    # TODO: check if sessionID is valid and studentID is valid
    return server_response(status=200, json=receivedData)


@app.route("/startSession", methods=["POST"])
def startSession():
    expectedData = ["lecturerID", "sessionTime", "sessionDate", "subjectID"]
    receivedData = request.get_json()

    try:
        receivedData = extract_required_data(receivedData, expectedData)
    except:
        print("[SERVER] - ERROR EXTRACTING LECTURE SESSION DATA")
        return server_response(status=500)

    sessionID = gen_code()
    columns = list(receivedData.keys())
    columns.insert(0, "sessionID")

    values = list(receivedData.values())
    values.insert(0, sessionID)

    try:
        insert_into_table("lectureSessions", columns, values)
    except:
        print("[SERVER] - ERROR INSERTING LECTURE SESSION INTO TABLE")
        return server_response(status=500)
    else:
        return server_response(status=200, json={"lectureSessionID": sessionID})


@app.route("/", methods=["GET"])
def testConnection():
    return server_response(status=200)


@app.route("/registerLecturer", methods=["POST"])
def register():
    expectedData = ["firstName", "lastName", "subjectIDs", "hashedPass"]
    receivedData = request.get_json()

    try:
        receivedData = extract_required_data(receivedData, expectedData)
    except:
        return server_response(status=500)

    lecturerID = gen_code()
    columns = list(receivedData.keys())
    columns.insert(0, "lecturerID")

    values = list(receivedData.values())
    values.insert(0, lecturerID)

    try:
        insert_into_table("lecturers", columns, values)
    except:
        return server_response(status=500)
    else:
        return server_response(status=200)


if __name__ == "__main__":
    app.run(port=3669)
