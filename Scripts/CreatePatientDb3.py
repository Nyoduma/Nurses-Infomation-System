#Create a TABLE
import sqlite3 # imports sqlite3
conn = sqlite3.connect('unit3.db') #opens db
print("Opened database successfully")
conn.execute('''CREATE TABLE patient
            (patient_id INTEGER PRIMARY KEY NOT NULL,
            first_name TEXT  NOT NULL,
            sir_name TEXT NOT  NULL,
            age INTEGER NOT NULL,
            height TEXT NOT  NULL,
            weight TEXT NOT NULL,
            bmi REAL NOT NULL,
            mobile_phone TEXT NOT  NULL,
            email TEXT UNIQUE NOT NULL,
            date_of_admission TEXT NOT NULL,
            condition CHAR(100) NOT  NULL,
            current_meds CHAR(100) NOT NULL,
            nursing_care CHAR(100) NOT NULL,
            medical_history CHAR(100) NOT NULL,
            doctor_id  INT NOT NULL,
            staff_id INT NOT  NULL,
            FOREIGN KEY(doctor_id) REFERENCES DOCTOR(doctorid)  
            FOREIGN KEY (staff_id) REFERENCES NURSES(staffid));''')
print("Table created successfully") #prints string to console
conn.close() #closes db
#reference to UNIQUE CONSTRAINT https://www.sqlitetutorial.net/sqlite-unique-constraint/