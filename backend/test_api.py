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
    def test_register_lecturer(self):
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
    def test_register_student(self):
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
    def test_login_student(self):
        input = {
            "userType": "student",
            "email": "davidsheen@why.brah",
            "hashedPass": "qwertyuio",
        }

        response = requests.post(f"{self.ENDPOINT}/login", json=input)
        pytest.studentUserSessionID = response.json()["userSessionKey"]
        assert response.status_code == 200

    @pytest.mark.order(5)
    def test_login_lecturer(self):
        input = {
            "userType": "lecturer",
            "hashedPass": "qwertyuio",
            "email": "richerd@why.no",
        }

        response = requests.post(f"{self.ENDPOINT}/login", json=input)
        pytest.lectuererUserSessionID = response.json()["userSessionKey"]
        assert response.status_code == 200

    @pytest.mark.order(6)
    def test_start_session(self):
        input = {
            "lecturerID": "sqbyc",
            "sessionStart": "2003-04-04 13:00",
            "sessionEnd": "2003-04-04 14:00",
            "subjectID": "testSession",
            "questionSource": "Richard and Mary are very good Friends",
            "userSessionID": pytest.lectuererUserSessionID,
        }

        response = requests.post(f"{self.ENDPOINT}/startSession", json=input)
        pytest.lecturesessionID = response.json()["lectureSessionID"]
        assert len(pytest.lecturesessionID) == 5

    @pytest.mark.order(7)
    def test_mark_attendace(self):
        input = {
            "email": "davidsheen@why.brah",
            "lectureSessionID": pytest.lecturesessionID,
            "userSessionID": pytest.studentUserSessionID,
        }

        response = requests.post(f"{self.ENDPOINT}/markAttendance", json=input)
        assert response.status_code == 200
