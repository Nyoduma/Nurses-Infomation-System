#Create a TABLE
import sqlite3 # imports the SQLite library
conn = sqlite3.connect('unit2.db') #opens database
print("Opened database successfully")
conn.execute('''CREATE TABLE PATIENT
            (PatientID INT PRIMARY KEY NOT NULL,
            FirstName   TEXT    NOT NULL,
            SurName   TEXT   NOT NULL,
            AGE   INT     NOT NULL,
            HEIGHT CHAR(10) NOT NULL,
            WEIGHT CHAR(10) NOT  NULL,
            BMI REAL NOT NULL,
            BSL REAL NOT NULL,
            ADDRESS   CHAR(50) NOT NULL,
            Mphone INT NOT NULL,
            EMAIL TEXT UNIQUE NOT NULL,
            DATEofAdmission TEXT NOT NULL,
            TIMEofAdmission TEXT NOT NULL,
            NextOfKin CHAR (20) NOT NULL,
            NextOfKinMobile INT NOT NULL,
            CONDITION CHAR(100) NOT NULL,
            CURRENTmeds CHAR(100) NOT NULL,
            NURSINGcare CHAR(100) NOT NULL,
            MEDICALhistory CHAR(100) NOT NULL,
            Doctor_ID INT NOT NULL,
            Staff_ID INT NOT NULL,
            FOREIGN KEY(Doctor_ID) REFERENCES DOCTOR(DoctorID)
            FOREIGN KEY (Staff_ID) REFERENCES NURSES(StaffID));''')
print("Table created successfully")

#conn.execute("ALTER TABLE PATIENT DROP COLUMN DoctorID") #referenced from https://www.sqlite.org/lang_altertable.html
#conn.execute('select PATIENT from sqlite_master where type="table"').fetchall()  # referenced from https://stackoverflow.com/questions/14262771/why-am-i-suddenly-getting-operationalerror-no-such-table
conn.close() # closes database
