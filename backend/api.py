from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    return jsonify({"userSessionID": "QEWUYBFQO8NFALSDIF"})


@app.route("/markAttendance", methods=["POST"])
def markAttendance():

    response = make_response()
    response.status_code = 200

    return response


@app.route("/startSession", methods=["POST"])
def startSession():
    expectedData = ["lecturerID", "time", "date", "subject"]
    receivedData = request.get_json()

    result = jsonify({"lectureSessionID": "xhqup"})
    return make_response(result)


@app.route("/", methods=["GET"])
def testConnection():

    response = make_response()
    response.status_code = 200
    return response


if __name__ == "__main__":
    app.run(port=3669)
