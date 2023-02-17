from flask import Flask, request
import json
import mysql.connector
import random, string

app = Flask(__name__)


def runDBQuery(query, val):
    with mysql.connector.connect(host="localhost", user="root", password="") as myDB:
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
        result = json.dumps({"error": ":("})
        return result
    else:
        result = json.dumps(receivedData)
        return result


@app.route("/startSession", methods=["POST"])
def startSession():
    expectedData = ["lecturerID", "time", "date", "moduleCode"]
    receivedData = request.get_json()

    data = extractRequiredData(receivedData, expectedData)
    sessionID = genCode()

    result = json.dumps({"sessionID": sessionID})
    return result


@app.route("/", methods=["GET"])
def testConnection():

    result = json.dumps({"result": "Connected Successfully"})
    return result


if __name__ == "__main__":

    app.run(port=3669)
