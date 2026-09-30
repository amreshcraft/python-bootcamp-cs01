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

## Multiple Data Insertion

```sql
INSERT INTO products VALUES (
  'Physics By DC Pandey', 1050,'Great book for self learning of physics!!!!'),
  ("C language by Reema Thareja",700, "Good book for indepth concept understanding");
```

### Update Data 

```sql
UPDATE products SET price = 699 WHERE price = 1050 ;
```

### Delete Data 

```sql
DELETE FROM products WHERE price = 699;
```

### Delete vs Drop vs TRUNCATE

- DELETE - specific data remove
- TRUNCATE - Delete all record from table but preserve table structure
- DROP - TABLE delete from database permanently


### TRUNCATE 
```sql
TRUNCATE TABLE products;
```

### DROP
```sql
DROP TABLE products;
```

## ALTER - Change Table structure
```sql
ALTER TABLE employees ADD email VARCHAR(100);
```

### RENAME

```sql
 ALTER TABLE majdoor  RENAME TO employees;
```