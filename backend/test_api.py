import requests
from dbFunctions import *
import unittest


class apiTests(unittest.TestCase):
    ENDPOINT = "http://127.0.0.1:5000"
    # ENDPOINT = "http://34.135.125.228"

    def test_check_api_connection(self):
        response = requests.get(f"{self.ENDPOINT}/")
        assert response.status_code == 200

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

    def test_login_student(self):
        email = "micheal@jackson.heehee"
        password = "qwertyuio"
        insert_into_table(
            "students",
            [
                "email",
                "firstName",
                "lastName",
                "subjectIDs",
                "hashedPass",
            ],
            [
                email,
                "Micheal",
                "Jackson",
                "Richard | Adam | Rick",
                password,
            ],
        )

        input = {
            "userType": "student",
            "hashedPass": password,
            "email": email,
        }

        response = requests.post(f"{self.ENDPOINT}/login", json=input)
        dbRow = get_row_from_table("students", "email", email)
        assert response.status_code == 200

    def test_login_lecturer(self):

        email = "test@testing.ahhhhhhhh"
        password = "qwertyuio"
        insert_into_table(
            "lecturers",
            [
                "email",
                "firstName",
                "lastName",
                "subjectIDs",
                "hashedPass",
            ],
            [
                email,
                "Micheal",
                "Jackson",
                "Richard | Adam | Rick",
                password,
            ],
        )

        input = {
            "userType": "lecturer",
            "hashedPass": password,
            "email": email,
        }

        response = requests.post(f"{self.ENDPOINT}/login", json=input)
        userSessionKey = response.json()["userSessionKey"]
        dbRow = get_row_from_table("lecturers", "email", email)
        assert response.status_code == 200

    def test_start_session(self):
        userSessionID = "gehrysxixm"
        expiry = "2030-04-04 22:00:49"
        lectuererID = "aaaaa"
        insert_into_table(
            "userSessions", ["userSessionID", "expiry"], [userSessionID, expiry]
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
        dbRow = get_row_from_table("lectureSessions", "lecturerID", lectuererID)
        assert len(lecturesessionID) == 5

    def test_mark_attendace(self):
        lecSessionID = "qwert"
        insert_into_table(
            "lectureSessions",
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
            "userSessions", ["userSessionID", "expiry"], [userSessionID, expiry]
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

    def test_get_questions(self):
        lecSessionID = "tyhgd"
        insert_into_table(
            "lectureSessions",
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

        questionID = ["12345", "12346"]
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
                questionID[0],
                "Who Art You?",
                "David",
                "Richard | Adam | Rick",
                lecSessionID,
            ],
        )

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
                questionID[1],
                "The Answer to Life, the Universe and Everything?",
                "42",
                "To Love | To Kill | 39",
                lecSessionID,
            ],
        )

        userSessionID = "gehrysxixq"
        expiry = "2030-04-04 22:00:49"
        insert_into_table(
            "userSessions", ["userSessionID", "expiry"], [userSessionID, expiry]
        )

        input = {
            "lectureSessionID": lecSessionID,
            "userSessionID": userSessionID,
        }

        response = requests.post(f"{self.ENDPOINT}/getQuestion", json=input)
        gotquestionID = response.json()["questionID"]
        assert response.status_code == 200 and gotquestionID in questionID

    def test_get_questions_not_ready(self):

        userSessionID = "gehrnuxixq"
        expiry = "2030-04-04 22:00:49"
        insert_into_table(
            "userSessions", ["userSessionID", "expiry"], [userSessionID, expiry]
        )

        input = {
            "lectureSessionID": "asdf",
            "userSessionID": userSessionID,
        }

        response = requests.post(f"{self.ENDPOINT}/getQuestion", json=input)
        questionsStatus = response.json()["questionsStatus"]
        assert response.status_code == 200 and questionsStatus == "not ready"

    def test_submit_answers(self):
        input = {
            "questionID": "Rich",
            "email": "richerd@why.no",
            "result": "Pass",
        }

        response = requests.post(f"{self.ENDPOINT}/submitAnswer", json=input)

        dbRow = get_row_from_table("studentAnswers", "email", "richerd@why.no")
        expected = ("Rich", "richerd@why.no", "Pass")
        assert response.status_code == 200 and dbRow[0] == expected
