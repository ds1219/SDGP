DROP DATABASE `sdgptest`;
CREATE DATABASE `sdgptest`;
USE sdgptest;
CREATE TABLE lectureSessions (sessionID varchar(5),
                              lecturerID varchar(5),
                              sessionTime time,
                              sessionDate date,
                              subjectID text,
                              questionSource text);
CREATE TABLE lecturers (email varchar (255), firstName text, lastName text, subjectIDs text, hashedPass text);
CREATE TABLE students (email varchar (255), firstName text, lastName text, subjectIDs text, hashedPass text);
CREATE TABLE subjects (subjectID varchar (5), subjectName text);
CREATE TABLE questions (questionID varchar (5), question text, sessionID varchar (5));
CREATE TABLE Attendance (studentID varchar(5), questionID varchar(5), answer text, pass BOOLEAN);