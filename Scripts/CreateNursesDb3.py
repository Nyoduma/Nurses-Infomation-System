#Create a TABLE
import sqlite3  #imports sqlite3
conn = sqlite3.connect('unit3.db') # opens db
print("Opened database successfully")
conn.execute('''CREATE TABLE NURSES
            (StaffID INT PRIMARY KEY NOT NULL,
            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL,
            Level TEXT NOT NULL,
            Mobile TEXT NOT NULL,
            Department TEXT NOT NULL,
            StartDate TEXT NOT NULL,
            Address CHAR(50) NOT NULL);''')
print("Table created successfully")
conn.close() #closes db
