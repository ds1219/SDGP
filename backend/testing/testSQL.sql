DROP DATABASE `sdgpTest`;
CREATE DATABASE `sdgpTest`;

USE `sdgpTest`;
CREATE TABLE lectureSessions (sessionID varchar(5),
                              lecturerID varchar(5),
                              sessionTime time,
                              sessionDate date,
                              subjectID text
                             );
CREATE TABLE lecturers (lecturerID varchar, firstName text, lastName text, subjects);
CREATE TABLE students (studentID, firstName, lastName, subjects)