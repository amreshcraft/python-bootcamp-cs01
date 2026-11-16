CREATE TABLE students (
id int not null,
name varchar(50) not null,
class int not null ,
marks float not null
);



INSERT INTO students VALUES
(2, 'Rohan', 12, 85.5),
(3, 'Priya', 11, 91.0),
(4, 'Sneha', 12, 74.5),
(5, 'Vikram', 10, 68.0),
(6, 'Ananya', 12, 94.5),
(7, 'Kabir', 11, 81.0),
(8, 'Meera', 10, 88.5),
(9, 'Aditya', 12, 62.0),
(10, 'Neha', 11, 79.5),
(11, 'Aryan', 10, 90.0);



CREATE TABLE captains (
    id int NOT NULL,
    name varchar(50) NOT NULL,
    post varchar(100) NOT NULL
);