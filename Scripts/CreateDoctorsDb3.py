#Create a TABLE
import sqlite3   #imports sqlite3
conn = sqlite3.connect('unit3.db') # opens database
print("Opened database successfully")
conn.execute('''CREATE TABLE DOCTORS
            (DoctorID INT PRIMARY KEY NOT NULL,
            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL,
            Speciality TEXT NOT NULL,
            BleepNo TEXT NOT NULL,
            PHONE TEXT NOT NULL);''')
print("Table created successfully")
conn.close()