CREATE DATABASE appdb;
GO

USE appdb;
GO

CREATE TABLE Candidates(
candidate_id INT PRIMARY KEY IDENTITY(1,1),
name VARCHAR(100),
age INT,
gender VARCHAR(10),
party VARCHAR(100),
constituency VARCHAR(100)

);
CREATE TABLE voters(
    voter_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(100),
    a
)