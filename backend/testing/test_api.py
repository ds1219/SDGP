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


# ClearDB
query = """ 
            /* Drop All Tables - https://www.databasestar.com/mysql-drop-all-tables/ */
            SET FOREIGN_KEY_CHECKS = 0;
            SET GROUP_CONCAT_MAX_LEN=32768;
            SET @tables = NULL;
            SELECT GROUP_CONCAT('`', table_name, '`') INTO @tables
            FROM information_schema.tables
            WHERE table_schema = (SELECT DATABASE());
            SELECT IFNULL(@tables,'dummy') INTO @tables;
            SET @tables = CONCAT('DROP TABLE IF EXISTS ', @tables);
            PREPARE stmt FROM @tables;
            EXECUTE stmt;
            DEALLOCATE PREPARE stmt;
            SET FOREIGN_KEY_CHECKS = 1;

            CREATE TABLE lectureSessions (sessionID varchar(5),lecturerID varchar(5),sessionTime time,sessionDate date,subjectID text);
            CREATE TABLE lecturers (lecturerID varchar (5), firstName text, lastName text, subjectIDs text, hashedPass text);
            CREATE TABLE students (studentID varchar(5), firstName text, lastName text, subjects text);
        """
run_db_query(query)


def test_check_api_connection():
    response = requests.get(f"{ENDPOINT}/")
    assert response.status_code == 200


# def test_mark_attendance():
def test_mark_attendace():
    input = {
        "studentID": "20030496",
        "questionID": "34",
        "answer": "Richard Stallman",
        "sessionID": "testSession",
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
