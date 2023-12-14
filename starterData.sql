CREATE DATABASE Students;
USE Students;

CREATE TABLE student (
  StudentID INT NOT NULL AUTO_INCREMENT,
  FirstName VARCHAR(100) NOT NULL,
  LastName VARCHAR(100) NOT NULL,
  PRIMARY KEY (StudentID)
);

INSERT INTO student (FirstName, LastName) VALUES
  ("John", "Smith"),
  ("Joseph", "Joestar"),
  ("Emma", "Stone");