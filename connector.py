import mysql.connector

cnx = mysql.connector.connect(
    user="your_username",
    password="your_password",
    host="your_hostname",
    database="sdgptest",
)
cursor = cnx.cursor()

query = "SELECT questionID FROM questions WHERE questionID = 'id';"
cursor.execute(query)
query = "DROP DATABASE `sdgptest`;"
cursor.execute(query)
query = "CREATE DATABASE `sdgptest`;"
cursor.execute(query)
query = "USE sdgptest;"
cursor.execute(query)
query = "CREATE TABLE lectureSessions (sessionID varchar(5), lecturerID varchar(5), sessionStart datetime, sessionEnd datetime, subjectID text, questionSource text);"
cursor.execute(query)
query = "CREATE TABLE lecturers (email varchar (255), firstName text, lastName text, subjectIDs text, hashedPass text);"
cursor.execute(query)
query = "CREATE TABLE students (email varchar (255), firstName text, lastName text, subjectIDs text, hashedPass text);"
cursor.execute(query)
query = "CREATE TABLE subjects (subjectID varchar(5), subjectName text);"
cursor.execute(query)
query = "CREATE TABLE questions (questionID varchar(5), question text, answer text, sessionID varchar(5));"
cursor.execute(query)
query = "CREATE TABLE answers (questionID varchar(5), email varchar(255));"
cursor.execute(query)
query = "CREATE TABLE attendance (email varchar(5), lectureSessionID varchar(5));"
cursor.execute(query)
query = "CREATE TABLE userSessions (userSessionID varchar(10), expiry datetime);"
cursor.execute(query)
query = "ALTER TABLE lectureSessions ADD lastQuestionGenerationTime datetime;"
cursor.execute(query)
query = "UPDATE lectureSessions SET lastQuestionGenerationTime = sessionStart;"
cursor.execute(query)

# FUNCTION statement
query = """
DELIMITER //
CREATE FUNCTION needs_new_questions(sessionID varchar(5)) RETURNS boolean
BEGIN
  DECLARE last_gen_time datetime;
  DECLARE elapsed_time int;
  
  SELECT lastQuestionGenerationTime INTO last_gen_time FROM lectureSessions WHERE sessionID = sessionID;
  
  SET elapsed_time = TIMESTAMPDIFF(MINUTE, last_gen_time, NOW());
  
  IF elapsed_time >= 5 THEN
    RETURN true;
  ELSE
    RETURN false;
  END IF;
END //
DELIMITER ;
"""
cursor.execute(query)


def execute_sql_query(query):
    cursor.execute(query)
    return cursor.fetchall()


def needs_new_questions(session_id):
    query = f"SELECT needs_new_questions('{session_id}')"
    result = execute_sql_query(query)
    return result[0][0]


query = "SELECT sessionID FROM lectureSessions WHERE sessionEnd > NOW() LIMIT 1;"
result = execute_sql_query(query)
while result:
    session_id = result[0][0]
    if needs_new_questions(session_id):
        query = f"UPDATE lectureSessions SET lastQuestionGenerationTime = NOW() WHERE sessionID = '{session_id}';"
        execute_sql_query(query)
    query = f"SELECT sessionID FROM lectureSessions WHERE sessionEnd > NOW() AND sessionID > '{session_id}' LIMIT 1;"
    result = execute_sql_query(query)
cursor.close()
cnx.close()
