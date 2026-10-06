
# Step by Step 

```py
python -m venv  .venv
```

## Activate
```py
source ./.venv/bin/activate.fish
```


## Install Mysql connector

```py
pip install mysql-connector-python
```


## DB

```sql 
CREATE DATABASE mario;
USE mario;
CREATE TABLE user (id INT , name VARCHAR(255), email VARCHAR(255), age INT );
```

## Insert 

```sql
INSERT INTO user (id, name, age, email) 
VALUES (1, 'Yuvraj', 16, 'yuvrajpro@gmail.com');
```
