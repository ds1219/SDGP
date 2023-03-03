import requests
import mysql.connector


def run_db_query(query):
    mydb = mysql.connector.connect(
        host="localhost", user="backend", password="b3k3nd", database="sdgpTest"
    )
    cursor = mydb.cursor()

    cursor.execute(query)
    cursor.close()
    mydb.close()


ENDPOINT = "http://127.0.0.1:3669"


def test_check_api_connection():
    response = requests.get(f"{ENDPOINT}/")
    assert response.status_code == 200


# def test_mark_attendance():
def test_mark_attendace():
    input = {
        "studentID": "dqpoi",
        "questionID": "34",
        "answer": "Richard Stallman",
        "lectureSessionID": "12345",
    }

    response = requests.post(f"{ENDPOINT}/markAttendance", json=input)
    assert response.json() == input


def test_start_session():
    input = {
        "lecturerID": "qwedt",
        "sessionTime": "13:00",
        "sessionDate": "2003-04-04",
        "subjectID": "testSession",
    }

    response = requests.post(f"{ENDPOINT}/startSession", json=input)
    assert len(response.json()["lectureSessionID"]) == 5


def test_registerLecturer():
    input = {
        "firstName": "David",
        "lastName": "Sheen",
        "subjectIDs": "12345-54321",
        "hashedPass": "qwertyuio",
        "entityName": "lecturer",
    }

    response = requests.post(f"{ENDPOINT}/register", json=input)
    assert response.status_code == 200


def test_registerStudent():
    input = {
        "firstName": "David",
        "lastName": "Sheen",
        "subjectIDs": "12345-54321",
        "hashedPass": "qwertyuio",
        "entityName": "student",
    }

    response = requests.post(f"{ENDPOINT}/register", json=input)
    assert response.status_code == 200
