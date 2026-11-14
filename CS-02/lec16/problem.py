CREATE DATABASE CINEMA;  -- create a database named CINEMA
USE CINEMA;  -- use the CINEMA database

CREATE TABLE THREATRE (
    TH_ID CHAR(5) NOT NULL ,
    Name VARCHAR(15) NOT NULL,
    City VARCHAR(15) NOT NULL,
    Location VARCHAR(15),
    Seats INT
);


import mysql.connector  as sql

mydb = sql.connect(host="localhost", user="root", password="1234", database="CINEMA")

TH_ID = input("Enter the Theatre ID to delete: ")

def Delete_Theatre():
    c = mydb.cursor()
    c.execute(f"DELETE FROM THREATRE WHERE TH_ID = '{TH_ID}';")
    mydb.commit()
    c.close()
    print("Theatre deleted successfully of id: ", TH_ID)
    

Delete_Theatre()