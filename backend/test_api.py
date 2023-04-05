import requests
from dbFunctions import *
import pytest
import unittest


class apiTests(unittest.TestCase):
    ENDPOINT = "http://127.0.0.1:5000"

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

        response = requests.post(f"{self.ENDPOINT}/register", json=input)

        dbRow = get_row_from_table("lecturers", "email", "richerd@why.no")
        expected = ("richerd@why.no", "Rich", "Erd", "12345-54321", "qwertyuio")
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
        dbRow = get_row_from_table("students", "email", "davidsheen@why.brah")
        expected = ("davidsheen@why.brah", "David", "Sheen", "12345-54321", "qwertyuio")
        assert response.status_code == 200 and dbRow[0] == expected

    @pytest.mark.order(4)
    def test_login_student(self):
        email = "davidsheen@why.brah"
        input = {
            "userType": "student",
            "email": email,
            "hashedPass": "qwertyuio",
        }

        response = requests.post(f"{self.ENDPOINT}/login", json=input)
        dbRow = get_row_from_table("students", "email", email)
        assert response.status_code == 200

    @pytest.mark.order(5)
    def test_login_lecturer(self):
        email = "richerd@why.no"
        input = {
            "userType": "lecturer",
            "hashedPass": "qwertyuio",
            "email": email,
        }

        response = requests.post(f"{self.ENDPOINT}/login", json=input)
        userSessionKey = response.json()["userSessionKey"]
        dbRow = get_row_from_table("lecturers", "email", email)
        assert response.status_code == 200

    @pytest.mark.order(6)
    def test_start_session(self):
        userSessionID = "gehrysxixm"
        expiry = "2030-04-04 22:00:49"
        lectuererID = "aaaaa"
        insert_into_table(
            "usersessions", ["userSessionID", "expiry"], [userSessionID, expiry]
        )
        input = {
            "lecturerID": lectuererID,
            "sessionStart": "2003-04-04 13:00",
            "sessionEnd": "2003-04-04 14:00",
            "subjectID": "testSession",
            "questionSource": "Richard and Mary are very good Friends",
            "userSessionID": userSessionID,
        }

        response = requests.post(f"{self.ENDPOINT}/startSession", json=input)
        lecturesessionID = response.json()["lectureSessionID"]
        dbRow = get_row_from_table("lecturesessions", "lecturerID", lectuererID)
        assert len(lecturesessionID) == 5

    @pytest.mark.order(7)
    def test_mark_attendace(self):
        lecSessionID = "qwert"
        insert_into_table(
            "lecturesessions",
            [
                "sessionID",
                "lecturerID",
                "sessionStart",
                "sessionEnd",
                "subjectID",
                "questionSource",
            ],
            [
                lecSessionID,
                "bbbbb",
                "2003-04-04 13:00",
                "2003-04-04 14:00",
                "test2",
                "Github is a Version Control Software",
            ],
        )

        userSessionID = "gehryerixm"
        expiry = "2030-04-04 22:00:49"
        insert_into_table(
            "usersessions", ["userSessionID", "expiry"], [userSessionID, expiry]
        )

        email = "davidsheen@why.brah"
        input = {
            "email": email,
            "lectureSessionID": lecSessionID,
            "userSessionID": userSessionID,
        }

        response = requests.post(f"{self.ENDPOINT}/markAttendance", json=input)
        dbRow = get_row_from_table("attendance", "email", email)
        assert response.status_code == 200

    @pytest.mark.order(8)
    def test_get_questions(self):
        insert_into_table(
            "lecturesessions",
            [
                "sessionID",
                "lecturerID",
                "sessionStart",
                "sessionEnd",
                "subjectID",
                "questionSource",
            ],
            [
                "qwert",
                "bbbbb",
                "2003-04-04 13:00",
                "2003-04-04 14:00",
                "test2",
                "Github is a Version Control Software",
            ],
        )

        lecSessionID = "qwert"
        questionID = "1234"
        insert_into_table(
            "questions",
            [
                "questionID",
                "question",
                "answer",
                "wrongAnswers",
                "sessionID",
            ],
            [
                questionID,
                "Who Art You?",
                "David",
                "Richard | Adam | Rick",
                lecSessionID,
            ],
        )

        userSessionID = "gehrysxixq"
        expiry = "2030-04-04 22:00:49"
        insert_into_table(
            "usersessions", ["userSessionID", "expiry"], [userSessionID, expiry]
        )

        email = "davidsheen@why.brah"
        input = {
            "lectureSessionID": lecSessionID,
            "userSessionID": userSessionID,
        }

        response = requests.post(f"{self.ENDPOINT}/getQuestion", json=input)

        assert (
            response.status_code == 200 and response.json()["questionID"] == questionID
        )
