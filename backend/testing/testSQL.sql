/* Run on Initial DB Setup*/
CREATE USER 'backend'@'localhost' IDENTIFIED BY 'b3k3nd';
CREATE DATABASE `sdgpTest`;
GRANT ALL PRIVILEGES ON sdgpTest.* TO 'backend'@'localhost';

/* Will Run Automatically On Test */
CREATE TABLE lectureSessions (sessionID varchar(5),
                              lecturerID varchar(5),
                              sessionTime time,
                              sessionDate date,
                              subjectID text
                             );
CREATE TABLE lecturers (lecturerID varchar (5), firstName text, lastName text, subjectIDs text, hashedPass text);
CREATE TABLE students (studentID varchar(5), firstName text, lastName text, subjects text);