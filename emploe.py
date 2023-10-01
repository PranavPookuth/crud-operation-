import mysql.connector

db=  mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="1234",
    database="empy"
)
c = db.cursor()
c.execute
#
# creating database

c.execute("CREATE DATABASE empy")


print("database created")

db.close()
#
#  create table
c.execute(
    """
    CREATE TABLE employee(
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,

    age INTEGER
    )
    """)
print("table is created")
db.close()

#insert into table
c.execute(
    """
    INSERT INTO employee VALUES
    (1, 'anu', 'anu@gmail.com',  31),
    (2, 'pj', 'pj@gmail.com',21),
    (3, 'jon', 'jon@gmail.com',37),
    (4, 'achu', 'achu@gmail.com',29)
    """)
print("rows are inserted")
db.commit()
db.close()


#read elements
c.execute("SELECT * FROM employee;")
result = c.fetchall()
# print(result)

for i in result:
    print(i)

#update
c.execute("update employee set age=29 where id=3")
db.commit()
print("updated")
db.close()


#delete
c.execute("delete from employee where id=4")
db.commit()
print("deleted")