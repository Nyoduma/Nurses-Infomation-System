#Create a TABLE
import sqlite3
conn = sqlite3.connect('unit2.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE DOCTORS
            (DoctorID INT PRIMARY KEY NOT NULL,
            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL,
            Speciality TEXT NOT NULL,
            BleepNo INT NOT NULL,
            PHONE TEXT NOT NULL);''')
print("Table created successfully")
conn.close()

#I am tacking the isert and select operation into another python file in order to make my code neat.










