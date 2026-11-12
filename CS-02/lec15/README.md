

# Database 

### show database

```sql
show databases;
```

### create database
```sql
create database hello;
```

### Use Database
```sql
use dbName;
```

### create tables
```sql
create table students (
rollno VARCHAR(255) PRIMARY KEY,
name VARCHAR(100) NOT NULL,
class INT NOT NULL,
gender VARCHAR(1) NOT NULL
);
```

### insert data 

```sql
INSERT INTO students (name,gender,class,rollno) VALUES ('Amresh','M',12,'hm420');
```

### Wrong code - order is mismatched
```sql
INSERT INTO students VALUES ('Amresh','M',12,'hm420');
```

### Corrected code - order matched
```sql
INSERT INTO students VALUES ('hm420','Amresh',,12,'M');
```