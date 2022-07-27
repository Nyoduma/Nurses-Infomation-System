#Create a TABLE
import sqlite3
conn = sqlite3.connect('unit.db')
print("Opened database successfully")
# conn.execute('''CREATE TABLE PATIENT
#           (PatientID INTEGER PRIMARY KEY AUTOINCREMENT,
#            FirstName   TEXT    NOT NULL,
#             SurName   TEXT   NOT NULL,
#             AGE        INT     NOT NULL,
#             HEIGHT CHAR(10) NOT NULL,
#             WEIGHT CHAR(10) NOT  NULL,
#             BMI REAL NOT NULL,
#             BSL REAL NOT NULL,
#             ADDRESS    CHAR(50) NOT NULL,
#             Mphone INT NOT NULL,
#             EMAIL TEXT UNIQUE NOT NULL,
#             DATEofAdmission DATETIME NOT NULL,
#             DOCTORname CHAR(20) NOT NULL,
#             NextOfKin CHAR (20) NOT NULL,
#             NextOfKinMobile INT NOT NULL,
#             CONDITION CHAR(200) NOT NULL,
#             CURRENTmeds CHAR(200) NOT NULL,
#             NURSINGcare CHAR(1000) NOT NULL,
#             MEDICALhistory CHAR(1000));''')
# print("Table created successfully")
conn.close

#INSERTING DETAILS INTO THE PATIENT TABLE

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
#              VALUES (1, 'Paul', 32, 'California', 20000.00 )");
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