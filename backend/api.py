from flask import Flask, request
import json, time
import mysql.connector

app = Flask(__name__)


def runDBQuery():
    # myDb = mysql.connector.connect(host="localhost", user="root", password="")
    # myCursor = myDb.cursor()
    return None


def extractRequiredData(receivedData, requiredData):
    outputData = {ed: receivedData[ed] for ed in requiredData}

    if len(outputData) != len(requiredData):
        raise Exception("Missing Values in POST")
    else:
        return outputData


@app.route("/markAttendance", methods=["POST"])
def markAttendance():
    inputData = {}
    expectedData = ["studentID", "questionID", "answer", "sessionID"]
    receivedData = request.get_json()

    try:
        receivedData = extractRequiredData(receivedData, expectedData)
    except:
        json_dump = json.dumps({"error": ":("})
        return json_dump
    else:
        json_dump = json.dumps(receivedData)
        return json_dump


@app.route("/", methods=["GET"])
def testConnection():

    json_dump = json.dumps({"result": "Connected Successfully"})

    return json_dump


if __name__ == "__main__":

    app.run(port=3669)
