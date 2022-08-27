#Create a TABLE
import sqlite3  #imports sqlite3
conn = sqlite3.connect('unit3.db')  # opens db
print("Opened database successfully")
conn.execute('''CREATE TABLE nurses
            (staffid INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT  NULL,
            last_name TEXT  NULL,
            password CHAR(6)  NULL,
            level TEXT  NULL,
            mobile TEXT  NULL,
            department TEXT NULL,
            Start_date TEXT  NULL,
            email TEXT UNIQUE NULL,
            address CHAR(50)  NULL);''')
print("Table created successfully")
conn.close() #closes db
