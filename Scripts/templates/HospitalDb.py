#Create a TABLE
import sqlite3
conn = sqlite3.connect('unit1.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE PATIENT
            (PatientID INTEGER PRIMARY KEY AUTOINCREMENT,
            FirstName   TEXT    NOT NULL,
            SurName   TEXT   NOT NULL,
            AGE        INT     NOT NULL,
            HEIGHT CHAR(10) NOT NULL,
            WEIGHT CHAR(10) NOT  NULL,
            BMI REAL NOT NULL,
            BSL REAL NOT NULL,
            ADDRESS    CHAR(50) NOT NULL,
            Mphone INT NOT NULL,
            EMAIL TEXT UNIQUE NOT NULL,
            DATEofAdmission TEXT NOT NULL,
            TIMEofAdmission TEXT NOT NULL,
            DoctorID INT NOT NULL,
            NextOfKin CHAR (20) NOT NULL,
            NextOfKinMobile INT NOT NULL,
            CONDITION CHAR(100) NOT NULL,
            CURRENTmeds CHAR(100) NOT NULL,
            NURSINGcare CHAR(500) NOT NULL,
            MEDICALhistory CHAR(500));''')
print("Table created successfully")
conn.close()


#INSERTING DETAILS INTO THE PATIENT TABLE
# import sqlite3
# conn = sqlite3.connect('unit1.db')
# print("Opened database successfully")
#
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT,WEIGHT,BMI,BSL,ADDRESS,Mphone, EMAIL,DATEofAdmission,"
#              "DOCTORname,NextOfKin,NextOfKinMobile,CONDITION,CURRENTmeds,NURSINGcare,MEDICALhistory)\
#               VALUES ('Paul','Butler' 32,175cm,90kg,29.4,4.5, '4 The Park,Ardee,County Louth',0877798711,'paul.butler@gmail.com,"
#              " 'California', 20000.00 )");
#
# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
#               VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
#
# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
#               VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
#
# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
#             VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
# conn.execute("INSERT INTO COMPANY (ID,NAME, AGE,ADDRESS,SALARY)\
#            VALUES (5,'Edith', 60, 'Drogheda', 85000.00)");
# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
#              VALUES (6, 'Vera', 32,'','')");

# conn.execute("INSERT INTO COMPANY (ID,NAME, AGE)\
#              VALUES(8,'Sam',30)");
#conn.close()