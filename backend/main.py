from flask import Flask, request
import json, time

app = Flask(__name__)


@app.route("/mark", methods=["POST"])
def markAttendance():
    """Mark the student's attendance

    Returns:
        string: json result
    """
    inputData = {}
    expectedData = ["studentID", "questionID", "answer", "sessionID"]
    receivedData = request.get_json()[ed]

    for ed in expectedData:
        inputData[ed] = receivedData

    json_dump = json.dumps(inputData)

    return json_dump


@app.route("/", methods=["GET"])
def testConnection():
    """test connection with the server

    Returns:
        string: _the result of the json
    """

    json_dump = json.dumps({"result": "Connected Successfully"})

    return json_dump


if __name__ == "__main__":
    app.run(port=3669)
