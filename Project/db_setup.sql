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
election_id INT PRIMARY KEY REFERENCES Elections(election_id),
voter_id

)