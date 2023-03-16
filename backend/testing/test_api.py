import requests

ENDPOINT = "http://127.0.0.1:5000"

studentUserSessionID = ""
lectuererUserSessionID = ""


def test_check_api_connection():
    response = requests.get(f"{ENDPOINT}/")
    assert response.status_code == 200


def test_registerLecturer():
    input = {
        "firstName": "Rich",
        "lastName": "Erd",
        "subjectIDs": "12345-54321",
        "hashedPass": "qwertyuio",
        "userType": "lecturer",
        "email": "richerd@why.no",
    }

    response = requests.post(f"{ENDPOINT}/register", json=input)
    assert response.status_code == 200


def test_registerStudent():
    input = {
        "firstName": "David",
        "lastName": "Sheen",
        "subjectIDs": "12345-54321",
        "hashedPass": "qwertyuio",
        "userType": "student",
        "email": "davidsheen@why.brah",
    }

    response = requests.post(f"{ENDPOINT}/register", json=input)
    assert response.status_code == 200


def test_loginStudent():
    input = {
        "userType": "student",
        "email": "davidsheen@why.brah",
        "hashedPass": "qwertyuio",
    }

    response = requests.post(f"{ENDPOINT}/login", json=input)
    studentUserSessionID = response.json()["userSessionKey"]
    assert response.status_code == 200


def test_loginLecturer():
    input = {
        "userType": "lecturer",
        "hashedPass": "qwertyuio",
        "email": "richerd@why.no",
    }

    response = requests.post(f"{ENDPOINT}/login", json=input)
    lectuererUserSessionID = response.json()["userSessionKey"]
    assert response.status_code == 200


# def test_mark_attendance():
def test_mark_attendace():
    input = {
        "studentID": "evobh",
        "questionID": "34",
        "answer": "Richard Stallman",
        "lectureSessionID": "12345",
        "userSessionID": studentUserSessionID,
    }

    response = requests.post(f"{ENDPOINT}/markAttendance", json=input)
    assert response.json() == input


def test_start_session():
    input = {
        "lecturerID": "sqbyc",
        "sessionTime": "13:00",
        "sessionDate": "2003-04-04",
        "subjectID": "testSession",
        "questionSource": "Richard and Mary are very good Friends",
        "userSessionID": lectuererUserSessionID,
    }

    response = requests.post(f"{ENDPOINT}/startSession", json=input)
    assert len(response.json()["lectureSessionID"]) == 5
