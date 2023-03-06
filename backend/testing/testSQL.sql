/* Run on Initial DB Setup*/
CREATE USER 'backend'@'localhost' IDENTIFIED BY 'b3k3nd';

/* run each time*/
DROP DATABASE `sdgpTest`;
CREATE DATABASE `sdgpTest`;
GRANT ALL PRIVILEGES ON sdgpTest.* TO 'backend'@'localhost';
USE sdgpTest;
CREATE TABLE lectureSessions (sessionID varchar(5),
                              lecturerID varchar(5),
                              sessionTime time,
                              sessionDate date,
                              subjectID text
                             );
CREATE TABLE lecturers (lecturerID varchar (5), firstName text, lastName text, subjectIDs text, hashedPass text);
CREATE TABLE students (studentID varchar (5), firstName text, lastName text, subjectIDs text, hashedPass text);
CREATE TABLE subjects (subjectID varchar (5), subjectName text);
CREATE TABLE questions (questionID varchar (5), question text, sourceID varchar (5));
CREATE TABLE Attendance (studentID varchar(5), questionID varchar(5), answer text, pass BOOLEAN);