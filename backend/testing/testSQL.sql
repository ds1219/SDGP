DROP DATABASE `sdpgTest`;
CREATE DATABASE `sdpgTest`;

USE `sdgptTest`;
CREATE TABLE lectureSessions (sessionID varchar(5), lecturerID varchar, sessionTime time, sessionDate date, subject text);
CREATE TABLE lecturers (lecturerID varchar, firstName text, lastName text, subjects);
CREATE TABLE students (studentID, firstName, lastName, subjects)