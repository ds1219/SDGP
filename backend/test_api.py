import requests

ENDPOINT = "http://127.0.0.1:3669"


def test_check_api_connection():
    response = requests.get(f"{ENDPOINT}/")
    assert response.status_code == 200


def test_mark_attendance():
    input = {
        "studentID": "20030496",
        "questionID": "34",
        "answer": "Richard Stallman",
        "sessionID": "testSession",
    }

    response = requests.post(f"{ENDPOINT}/markAttendance", json=input)

    print(response.json())
    assert response.json() == input


def test_start_session():
    input = {
        "lecturerID": "qwedt",
        "time": "13:00",
        "date": "2003-04-04",
        "subject": "testSession",
    }

    response = requests.post(f"{ENDPOINT}/startSession", json=input)

    print(response.json())
    assert len(response.json()["lectureSessionID"]) == 5
