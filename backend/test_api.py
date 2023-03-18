import requests
from dbFunctions import *
import pytest
import unittest


class apiTests(unittest.TestCase):
    ENDPOINT = "http://127.0.0.1:5000"

    studentUserSessionID = ""
    lectuererUserSessionID = ""

    @pytest.mark.order(1)
    def test_check_api_connection(self):
        response = requests.get(f"{self.ENDPOINT}/")
        assert response.status_code == 200

    @pytest.mark.order(2)
    def test_registerLecturer(self):
        input = {
            "firstName": "Rich",
            "lastName": "Erd",
            "subjectIDs": "12345-54321",
            "hashedPass": "qwertyuio",
            "userType": "lecturer",
            "email": "richerd@why.no",
        }

        expected = ("richerd@why.no", "Rich", "Erd", "12345-54321", "qwertyuio")

        response = requests.post(f"{self.ENDPOINT}/register", json=input)
        dbRow = get_row_from_table("lecturers", "email", "richerd@why.no")
        print(dbRow[0])

        assert response.status_code == 200 and dbRow[0] == expected

    @pytest.mark.order(3)
    def test_registerStudent(self):
        input = {
            "firstName": "David",
            "lastName": "Sheen",
            "subjectIDs": "12345-54321",
            "hashedPass": "qwertyuio",
            "userType": "student",
            "email": "davidsheen@why.brah",
        }

        response = requests.post(f"{self.ENDPOINT}/register", json=input)
        assert response.status_code == 200

    @pytest.mark.order(4)
    def test_loginStudent(self):
        input = {
            "userType": "student",
            "email": "davidsheen@why.brah",
            "hashedPass": "qwertyuio",
        }

        response = requests.post(f"{self.ENDPOINT}/login", json=input)
        pytest.studentUserSessionID = response.json()["userSessionKey"]
        assert response.status_code == 200

    @pytest.mark.order(5)
    def test_loginLecturer(self):
        input = {
            "userType": "lecturer",
            "hashedPass": "qwertyuio",
            "email": "richerd@why.no",
        }

        response = requests.post(f"{self.ENDPOINT}/login", json=input)
        pytest.lectuererUserSessionID = response.json()["userSessionKey"]
        assert response.status_code == 200

    @pytest.mark.order(6)
    def test_mark_attendace(self):
        input = {
            "studentID": "evobh",
            "questionID": "34",
            "answer": "Richard Stallman",
            "lectureSessionID": "12345",
            "userSessionID": pytest.studentUserSessionID,
        }

        response = requests.post(f"{self.ENDPOINT}/markAttendance", json=input)
        assert response.json() == input

    @pytest.mark.order(7)
    def test_start_session(self):
        input = {
            "lecturerID": "sqbyc",
            "sessionTime": "13:00",
            "sessionDate": "2003-04-04",
            "subjectID": "testSession",
            "questionSource": "Richard and Mary are very good Friends",
            "userSessionID": pytest.lectuererUserSessionID,
        }

        response = requests.post(f"{self.ENDPOINT}/startSession", json=input)
        assert len(response.json()["lectureSessionID"]) == 5
