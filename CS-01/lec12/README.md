# SQL

## Login in Shell 

## Linux 
```bash
sudo mysql -u userName -p
```

## Windows - CMD / Powershell

```bash
mysql -u userName -p
```

## Show / List Database
```sql
show databases;
```

## create database 
```sql
CREATE database dbName;
```


## To use Database

```sql
use dbName;
```

## To Show / List Tables

```sql
show tables;
```

## Create tables 

```sql
CREATE TABLE Employees (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER,
  salary REAL
);
```

## Read / View / Get / Retreive 
```sql
SELECT * FROM products;
```
```sql
SELECT title,price FROM products;
```

## Insert - Data

```sql
INSERT INTO products VALUES ('Maths By RD Sharma', 720,'Great book for self learning!!!!');
```