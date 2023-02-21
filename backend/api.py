from flask import Flask, request, make_response, jsonify
from helperFunctions import *

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    userSessionID = ""
    # TODO: Authenticate the user
    return jsonify({"userSessionID": userSessionID})


@app.route("/markAttendance", methods=["POST"])
def markAttendance():
    expectedData = ["studentID", "questionID", "answer", "sessionID"]
    receivedData = request.get_json()

    try:
        receivedData = extractRequiredData(receivedData, expectedData)
    except:
        return make_response(400)
    else:
        return make_response(jsonify(receivedData))


@app.route("/startSession", methods=["POST"])
def startSession():
    expectedData = ["lecturerID", "time", "date", "subject"]
    receivedData = request.get_json()

    data = extractRequiredData(receivedData, expectedData)
    sessionID = genCode()

    sqlQuery = "INSERT INTO sessions (sessionID, lecturerID, sessionTime, sessionDate, subject) VALUES (%s, %s, %s, %s, %s);"

    values = (sessionID,) + dictionaryToTuple(data)
    runDBQuery(sqlQuery, values)

    result = jsonify({"lectureSessionID": sessionID})
    return make_response(result)


@app.route("/", methods=["GET"])
def testConnection():

    response = make_response()
    response.status_code = 200
    return response


if __name__ == "__main__":
    app.run(port=3669)
