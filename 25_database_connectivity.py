# Python Database API (DB-API) is a standard interface to interact with various databases.
# DB-API supports connecting to different database servers such as Microsoft SQL Server 2000, PostgreSQL, Oracle.
# Different DB APIs are used for accessing different databases.
# Hence, a programmer has to install DB API corresponding to the database one is working with.


# Working with a database includes the following steps:
# Importing the corresponding DB-API module.
# Acquiring a connection with the database.
# Executing SQL statements and stored procedures.
# Closing the connection


# Using sqlite3, DB API for SQLite database:
# sqlite3 is available by default in Python standard library and hence there is no need of installing it separately.
# SQLite is a very lightweight database. You can connect to it directly, with minimal settings.

# Creating a Sample Table:
import sqlite3


# # establishing  a database connection
con = sqlite3.connect("TEST.db")
# # preparing a cursor object
cursor = con.cursor()
# # preparing sql statements
sql1 = "DROP TABLE IF EXISTS EMPLOYEE"
sql2 = """
       CREATE TABLE EMPLOYEE (
       EMPID INT(6) NOT NULL,
       NAME CHAR(20) NOT NULL,
       AGE INT,
       SEX CHAR(1),
       INCOME FLOAT
       )
      """

# executing sql statements
cursor.execute(sql1)
cursor.execute(sql2)

# closing the connection
con.close()


# Inserting Data:
# You created your table Now, let us learn how to insert data into the table.
# Data stored in Python variables can be inserted into database tables.
# Data is passed to SQL statements through parameter substitution.
# Single rows are inserted using 'execute' and multiple rows using 'executeMany' method of created cursor object.

# establishing the connection
con = sqlite3.connect("TEST.db")
# preparing a cursor object
cursor = con.cursor()
# preparing sql statement
rec = (456789, "Frodo", 45, "M", 100000.00)
sql = """
      INSERT INTO EMPLOYEE VALUES ( ?, ?, ?, ?, ?)
      """

# executing sql statement using try ... except blocks
try:
    cursor.execute(sql, rec)
    con.commit()
except Exception as e:
    print("Error Message :", str(e))
    con.rollback()


# Inserting Multiple records:

# preparing sql statement
records = [
    (123456, "John", 25, "M", 50000.00),
    (234651, "Juli", 35, "F", 75000.00),
    (345121, "Fred", 48, "M", 125000.00),
    (562412, "Rosy", 28, "F", 52000.00),
]

sql = """
       INSERT INTO EMPLOYEE VALUES ( ?, ?, ?, ?, ?)
      """
# executing sql statement using try ... except blocks
try:
    cursor.executemany(sql, records)
    con.commit()
except Exception as e:
    print("Error Message :", str(e))
    con.rollback()


# Fetching Data:
# After executing the SQL statement for reading records from a table, either of the following methods
# can be used to retrieve them in python.
# fetchone: It retrieves one record at a time in the form of a tuple.
# fetchall: It retrieves all fetched records at a point in the form of tuple of tuples.
sql = """
       SELECT * FROM EMPLOYEE
      """
# executing the sql statement using `try ... except`
try:
    cursor.execute(sql)
except Exception as e:
    print("Error Message :", str(e))

# fetching the records
records = cursor.fetchall()
# Displaying the records
for record in records:
    print(record)

# closing the connection
con.close()

# The above example fetches and displays all five records inserted into EMPLOYEE.
# Similarly, you can perform updating or delete records by preparing required SQL statements.


# Object Relational Mappers:
# An object-relational mapper (ORM) is a library that automates the transfer of data stored in relational database
# tables into objects that are adopted in application code.
# ORMs offer a high-level abstraction upon a relational database, which permits a developer to write Python code
# rather than SQL to create, read, update and delete data and schemas in their database.

# Sample ORM Query:

# Consider the sample SQL statement used to retrieve employees whose income is 10,000.00.
# SELECT * FROM EMPLOYEE WHERE INCOME=10000.00

# The equivalent Django ORM query is
# emps = Employee.objects.filter(income=10000.00)

# The above code is written in Python and easy to read.
# Such an ability to write Python code instead of SQL speeds up web application development.
# ORMs: Django, flask
