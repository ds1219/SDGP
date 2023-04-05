SELECT questionID FROM questions WHERE questionID = 'your_question_id';
DROP DATABASE `sdgptest`;
CREATE DATABASE `sdgptest`;
USE sdgptest;
CREATE TABLE lectureSessions (sessionID varchar(5),
                              lecturerID varchar(5),
                              sessionStart datetime,
                              sessionEnd datetime,
                              subjectID text,
                              questionSource text);
CREATE TABLE lecturers (email varchar (255), firstName text, lastName text, subjectIDs text, hashedPass text);
CREATE TABLE students (email varchar (255), firstName text, lastName text, subjectIDs text, hashedPass text);
CREATE TABLE subjects (subjectID varchar (5), subjectName text);
CREATE TABLE questions (questionID varchar (5), question text, answer text, sessionID varchar (5));
CREATE TABLE answers (questionID varchar (5), email varchar (255));
CREATE TABLE attendance (email varchar(5), lectureSessionID varchar(5));
CREATE TABLE userSessions (userSessionID varchar(10), expiry datetime);   how to check if need to generate new questions in every 5 minitues

ALTER TABLE lectureSessions ADD lastQuestionGenerationTime datetime;
UPDATE lectureSessions SET lastQuestionGenerationTime = sessionStart;

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
SET @sessionID = NULL;
SELECT sessionID INTO @sessionID FROM lectureSessions WHERE sessionEnd > NOW() LIMIT 1;

WHILE @sessionID IS NOT NULL DO
  IF needs_new_questions(@sessionID) THEN
    UPDATE lectureSessions SET lastQuestionGenerationTime = NOW() WHERE sessionID = @sessionID;
  END IF;
  
  SET @sessionID = NULL;
  SELECT sessionID INTO @sessionID FROM lectureSessions WHERE sessionEnd > NOW() AND sessionID > @sessionID LIMIT 1;
END WHILE;
