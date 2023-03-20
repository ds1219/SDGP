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
CREATE TABLE userSessions (userSessionID varchar(10), expiry datetime);