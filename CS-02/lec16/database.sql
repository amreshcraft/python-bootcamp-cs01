 mysql -u root -p

CREATE DATABASE CINEMA;  -- create a database named CINEMA
USE CINEMA;  -- use the CINEMA database

CREATE TABLE THREATRE (
    TH_ID CHAR(5) NOT NULL ,
    Name VARCHAR(15) NOT NULL,
    City VARCHAR(15) NOT NULL,
    Location VARCHAR(15),
    Seats INT
);


CREATE TABLE THREATRE (
    TH_ID CHAR(5) NOT NULL ,Name VARCHAR(15) NOT NULL,City VARCHAR(15) NOT NULL,Location VARCHAR(15),Seats INT
);

INSERT INTO THREATRE (TH_ID, Name, City, Location, Seats) VALUES
('T001', 'PVR', 'Bangalore', 'MG Road', 200),
('T002', 'INOX', 'Bangalore', 'Brigade Road', 150),
('T003', 'Cinepolis', 'Bangalore', 'Whitefield', 180),
('T004', 'PVR', 'Mumbai', 'Andheri', 220),
('T005', 'INOX', 'Mumbai', 'Bandra', 160),
('T006', 'Cinepolis', 'Mumbai', 'Juhu', 190);