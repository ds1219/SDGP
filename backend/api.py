from flask import Flask, request, make_response, jsonify
import mysql.connector
import random, string

app = Flask(__name__)


def dictionaryToTuple(dic):
    result = tuple(list(dic.values()))
    return result


def runDBQuery(query, val):
    with mysql.connector.connect(
        host="localhost", user="root", password="", database="sdgp test"
    ) as myDB:
        myCursor = myDB.cursor()
        myCursor.execute(query, val)


def genCode():
    length = 5
    newCode = ""
    for i in range(length):
        newCode += random.choice(string.ascii_lowercase)
    return newCode


def extractRequiredData(receivedData, requiredData):
    outputData = {ed: receivedData[ed] for ed in requiredData}

    if len(outputData) != len(requiredData):
        raise Exception("Missing Values in POST")
    else:
        return outputData


@app.route("/markAttendance", methods=["POST"])
def markAttendance():
    expectedData = ["studentID", "questionID", "answer", "sessionID"]
    receivedData = request.get_json()

    try:
        receivedData = extractRequiredData(receivedData, expectedData)
    except:
        result = {"error": ":("}
    else:
        result = receivedData

    result = jsonify(result)
    return make_response(result)


@app.route("/startSession", methods=["POST"])
def startSession():
    expectedData = ["lecturerID", "time", "date", "moduleCode"]
    receivedData = request.get_json()

    data = extractRequiredData(receivedData, expectedData)
    sessionID = genCode()

    sqlQuery = "INSERT INTO sessions (sessionID, lecturerID, time, date, moduleCode) VALUES ( %s %s %s %s %s)"

    values = (sessionID,) + dictionaryToTuple(data)
    print(values)
    runDBQuery(sqlQuery, values)

    result = jsonify({"sessionID": sessionID})
    return make_response(result)


@app.route("/", methods=["GET"])
def testConnection():

    response = make_response()
    response.status_code = 200
    return response


if __name__ == "__main__":
    app.run(port=3669)
