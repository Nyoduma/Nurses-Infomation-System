# conn.execute('''CREATE TABLE PATIENT
#             (PatientID INTEGER PRIMARY KEY AUTOINCREMENT,
#             FirstName   TEXT    NOT NULL,
#             SurName   TEXT   NOT NULL,
#             AGE        INT     NOT NULL,
#             HEIGHT CHAR(10) NOT NULL,
#             WEIGHT CHAR(10) NOT  NULL,
#             BMI REAL NOT NULL,
#             BSL REAL NOT NULL,
#             ADDRESS    CHAR(50) NOT NULL,
#             Mphone INT NOT NULL,
#             EMAIL TEXT UNIQUE NOT NULL,
#             DATEofAdmission TEXT NOT NULL,
#             TIMEofAdmission TEXT NOT NULL,
#             DoctorID INT NOT NULL,
#             NextOfKin CHAR (20) NOT NULL,
#             NextOfKinMobile INT NOT NULL,
#             CONDITION CHAR(100) NOT NULL,
#             CURRENTmeds CHAR(100) NOT NULL,
#             NURSINGcare CHAR(500) NOT NULL,
#             MEDICALhistory CHAR(500) NOT NULL);''')
# print("Table created successfully")
# conn.close()
