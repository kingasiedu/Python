import sqlite3
from sqlite3 import Error


# Connect to Database
def sql_connection():
    try:
        con = sqlite3.connect('Emplid1.db')
        return con
    except Error:
        print(Error)


# def sql_table(con):
# def sql_insert(con, entities):
#def sql_update(con):
def sql_fetch(con):
    cursorObj = con.cursor()
    # Create a table
    # cursorObj.execute(
    # "CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
    # Insert a table
    # cursorObj.execute(
    # "INSERT INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')")
    # cursorObj.execute("INSERT INTO employees(id, name, salary, department, position, hireDate)  VALUES(?,?,?,?,?,?)", entities)
    # Update the table it to Rogers 
    #cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
    #Fetch all data using fetchall()
    #It also prints out our record in our database
    #cursorObj.execute('SELECT * FROM employees')
    #Selects id and name that their salary is greater then $800
    #cursorObj.execute('SELECT id, name FROM employees WHERE salary > 800.0')
    #List table
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
    print(cursorObj.fetchall())
    #rows = cursorObj.fetchall()
    #for row in rows:
        #print(row)
    # con.commit to save changes
    con.commit()


con = sql_connection()
sql_fetch(con)

# entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
# con = sql_connection()
# sql_insert(con, entities)

# con = sql_connection()

# sql_table(con)
