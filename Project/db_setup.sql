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
CREATE TABLE Voters(
    voter_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    phone VARCHAR(20),
    constituency VARCHAR(100)
);
CREATE TABLE Elections(
election_id INT PRIMARY KEY IDENTITY(1,1),
election_name VARCHAR(100),
election_date VARCHAR(50),
constituency VARCHAR(100),
status VARCHAR(20) DEFAULT 'UPCOMING'
);