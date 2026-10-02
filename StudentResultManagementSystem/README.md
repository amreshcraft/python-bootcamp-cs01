# Project 1

## Create venv
```bash
python -m venv .venv
```

## Source Activate
```bash 
source ./.venv/bin/activate
```

## If requirements.txt file exist
```bash
pip install -r requirements.txt
```

## MySQL connector
```bash
pip install mysql-connector-python
```

## Create Database in MYSQL 
```bash
CREATE DATABASE students;
```

## Create Table 

```sql
CREATE TABLE chhatr (
    name VARCHAR(100) NOT NULL,
    class INT NOT NULL CHECK (class >= 1 AND class <= 12),
    rollno INT NOT NULL CHECK (rollno > 0),
    english INT NOT NULL CHECK (english >= 0 AND english <= 100), 
    physics INT NOT NULL CHECK (physics >= 0 AND physics <= 100), 
    maths INT NOT NULL CHECK (maths >= 0 AND maths <= 100), 
    chemistry INT NOT NULL CHECK (chemistry >= 0 AND chemistry <= 100), 
    cs INT NOT NULL CHECK (cs >= 0 AND cs <= 100), 
    obtained INT NOT NULL CHECK (obtained >= 0 AND obtained <= 500),
    max_marks INT NOT NULL DEFAULT max_marks = 500,
    percentage FLOAT NOT NULL CHECK (percentage >= 0 AND percentage <= 100 )
);
```