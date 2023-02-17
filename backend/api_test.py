import requests

#
response = requests.get("http://localhost:3669/")
print(response.json())

response = requests.post(
    "http://localhost:3669/markAttendance",
    json={
        "studentID": "20030496",
        "questionID": "34",
        "answer": "Richard Stallman",
        "sessionID": "testSession",
    },
)
print(response.json())

response = requests.post(
    "http://localhost:3669/startSession",
    json={
        "lecturerID": "20030496",
        "time": "34",
        "date": "Richard Stallman",
        "moduleCode": "testSession",
    },
)
print(response.json())
