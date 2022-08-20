#Create a TABLE
import sqlite3  #imports sqlite3
conn = sqlite3.connect('unit3.db') # opens db
print("Opened database successfully")
conn.execute('''CREATE TABLE nurses
            (staffid INT PRIMARY KEY NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            password CHAR(6) NOT NULL,
            level TEXT NOT NULL,
            mobile TEXT NOT NULL,
            department TEXT NOT NULL,
            Start_date TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            address CHAR(50) NOT NULL);''')
print("Table created successfully")
conn.close() #closes db
