#Create a TABLE
import sqlite3 # imports sqlite3
conn = sqlite3.connect('unit3.db') #opens db
print("Opened database successfully")
conn.execute('''CREATE TABLE patient
            (patient_id INTEGER PRIMARY KEY NULL,
            first_name TEXT NULL,
            sir_name TEXT NULL,
            age INTEGER NULL,
            height TEXT  NULL,
            weight TEXT  NULL,
            bmi REAL NULL,
            mobile_phone TEXT NULL,
            email TEXT UNIQUE NULL,
            date_of_admission TEXT NULL,
            condition CHAR(100) NULL,
            current_meds CHAR(100)  NULL,
            nursing_care CHAR(100) NULL,
            medical_history CHAR(100) NULL,
            doctor_id INT  NULL,
            staff_id INT NULL,
            FOREIGN KEY(doctor_id) REFERENCES DOCTOR(doctorid)  
            FOREIGN KEY (staff_id) REFERENCES NURSES(staffid));''')
print("Table created successfully") #prints string to console
conn.close() #closes db
#reference to UNIQUE CONSTRAINT https://www.sqlitetutorial.net/sqlite-unique-constraint/