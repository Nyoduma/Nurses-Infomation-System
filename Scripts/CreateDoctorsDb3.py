#Create a TABLE
import sqlite3   #imports sqlite3
conn = sqlite3.connect('unit3.db') # opens database
print("Opened database successfully")
conn.execute('''CREATE TABLE doctors
            (doctorid INT PRIMARY KEY NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            speciality TEXT NOT NULL,
            bleep_no TEXT NOT NULL,
            phone TEXT NOT NULL);''')
print("Table created successfully")
conn.close()