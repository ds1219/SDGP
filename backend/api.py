from flask import Flask, request, make_response, jsonify
from helperFunctions import *

app = Flask(__name__)

# TODO : ADD USER AUTH


@app.route("/login", methods=["POST"])
def login():
    expectedData = ["username", "hashedPassword"]
    receivedData = request.get_json()

    try:
        receivedData = extractRequiredData(receivedData, expectedData)
    except:
        return make_response(500)
    else:
        userSessionID = ""
        return jsonify({"userSessionID": userSessionID})


@app.route("/markAttendance", methods=["POST"])
def markAttendance():
    expectedData = ["studentID", "answer", "questionID", "lectureSessionID"]
    receivedData = request.get_json()

    try:
        receivedData = extractRequiredData(receivedData, expectedData)
    except:
        return make_response(400)

    query = 'SELECT * FROM Lecturer WHERE EXISTS(SELECT * From Lecturer WHERE lecturerID LIKE "%s")'

    # TODO: check if sessionID is valid and studentID is valid
    return make_response(jsonify(receivedData))


@app.route("/startSession", methods=["POST"])
def startSession():
    expectedData = ["lecturerID", "sessionTime", "sessionDate", "subjectID"]
    receivedData = request.get_json()

    try:
        receivedData = extractRequiredData(receivedData, expectedData)
    except:
        return make_response(400)

    sessionID = genCode()
    columns = list(receivedData.keys())
    columns.insert(0, "sessionID")

    values = list(receivedData.values())
    values.insert(0, sessionID)

    try:
        InsertIntoTable("lectureSessions", columns, values)
    except:
        response = make_response()
        response.status_code = 500
        return response
    else:
        result = jsonify({"lectureSessionID": sessionID})
        result = make_response(result)
        result.status_code = 200
        return make_response(result)


@app.route("/", methods=["GET"])
def testConnection():

    response = make_response()
    response.status_code = 200
    return response


if __name__ == "__main__":
    app.run(port=3669)
