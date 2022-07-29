#Create a TABLE
import sqlite3 # imports sqlite3
conn = sqlite3.connect('unit3.db') #opens db
print("Opened database successfully")
conn.execute('''CREATE TABLE PATIENT
            (PatientID INTEGER PRIMARY KEY NOT NULL,
            FirstName   TEXT    NOT NULL,
            SurName   TEXT   NOT NULL,
            AGE   INTEGER     NOT NULL,
            HEIGHT TEXT NOT NULL,
            WEIGHT TEXT NOT  NULL,
            BMI REAL NOT NULL,
            BSL REAL NOT NULL,
            ADDRESS   CHAR(50) NOT NULL,
            Mphone TEXT NOT NULL,
            EMAIL TEXT UNIQUE NOT NULL,
            DATEofAdmission TEXT NOT NULL,
            TIMEofAdmission TEXT NOT NULL,
            NextOfKin TEXT  NOT NULL,
            NextOfKinMobile TEXT NOT NULL,
            CONDITION CHAR(100) NOT NULL,
            CURRENTmeds CHAR(100) NOT NULL,
            NURSINGcare CHAR(100) NOT NULL,
            MEDICALhistory CHAR(100) NOT NULL,
            Doctor_ID INT NOT NULL,
            Staff_ID INT NOT NULL,
            FOREIGN KEY(Doctor_ID) REFERENCES DOCTOR(DoctorID)  
            FOREIGN KEY (Staff_ID) REFERENCES NURSES(StaffID));''')
print("Table created successfully")
conn.close() #closes db
#reference to UNIQUE CONSTRAINT https://www.sqlitetutorial.net/sqlite-unique-constraint/