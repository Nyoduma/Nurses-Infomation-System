#Create a TABLE
# import sqlite3
# conn = sqlite3.connect('unit2.db')
# print("Opened database successfully")
# conn.execute('''CREATE TABLE DOCTORS
#             (DoctorID INT PRIMARY KEY NOT NULL,
#             FirstName TEXT NOT NULL,
#             LastName TEXT NOT NULL,
#             Speciality TEXT NOT NULL,
#             BleepNo INT NOT NULL,
#             PHONE TEXT NOT NULL);''')
# print("Table created successfully")
# conn.close()



#INSERTING DETAILS INTO THE DOCTORS TABLE
import sqlite3
conn = sqlite3.connect('unit2.db')
print("Opened database successfully")
# conn.execute("INSERT INTO DOCTORS (DoctorID,FirstName,LastName, Speciality,BleepNo, PHONE)\
#               VALUES (1,' Caroline', 'Amenya', 'Oncology', 130,'0870975678')");

# conn.execute("INSERT INTO DOCTORS (DoctorID,FirstName,LastName, Speciality,BleepNo, PHONE)\
#               VALUES (2,' Judy', 'Wambui', 'Dermatology', 101,'0890975667')");
# conn.execute("INSERT INTO DOCTORS (DoctorID,FirstName,LastName, Speciality,BleepNo, PHONE)\
#               VALUES (3,' Sarah', 'Liberman', 'Orthopaedics', 1,'0870075678')");
# conn.execute("INSERT INTO DOCTORS (DoctorID,FirstName,LastName, Speciality,BleepNo, PHONE)\
#               VALUES (4,'Sandra ', 'Murphy', 'Gynaecology', 13,'0860925478')");
# conn.execute("INSERT INTO DOCTORS (DoctorID,FirstName,LastName, Speciality,BleepNo, PHONE)\
#               VALUES (5,' Zack', 'Omondi', 'ortolaryngology', 100,'0870975111')");
# conn.execute("INSERT INTO DOCTORS (DoctorID,FirstName,LastName, Speciality,BleepNo, PHONE)\
#               VALUES (6,' James', 'Ajimo', 'Renal', 122,'0898455678')");
# conn.execute("INSERT INTO DOCTORS (DoctorID,FirstName,LastName, Speciality,BleepNo, PHONE)\
#               VALUES (7,' Sylvia', 'Anderson', 'Medical', 17,'0850975678')");
# conn.execute("INSERT INTO DOCTORS (DoctorID,FirstName,LastName, Speciality,BleepNo, PHONE)\
#               VALUES (8,' Kendra', 'Allando', 'surgical', 150,'0870973331')");
# conn.execute("INSERT INTO DOCTORS (DoctorID,FirstName,LastName, Speciality,BleepNo, PHONE)\
#               VALUES (9,' Joseph', 'Butler', 'Cardiology', 16,'0870957896')");
# conn.execute("INSERT INTO DOCTORS (DoctorID,FirstName,LastName, Speciality,BleepNo, PHONE)\
#               VALUES (10,' Nathan', 'Butler', 'psychiatry', 155,'0870879578')");
#



conn.commit()
print("Records Created Successfully")
conn.close()







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
#             MEDICALhistory CHAR(500));''')
# print("Table created successfully")
# conn.close()




#INSERTING DETAILS INTO THE PATIENT TABLE
# import sqlite3
# conn = sqlite3.connect('unit1.db')
# print("Opened database successfully")
#
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT,WEIGHT,BMI,BSL,ADDRESS,Mphone, EMAIL,DATEofAdmission,
#               "TIMEOfAdmission,DoctorID,NextOfKin,NextOfKinMobile,CONDITION,CURRENTmeds,NURSINGcare,MEDICALhistory)\
#                VALUES ('Paul','Butler' 32,175cm,90kg,29.4,4.5, '4 The Park,Ardee,County Louth',0877798711,'paul.butler@gmail.com,"
#               "'2022/07/15','09.00hrs',5,'Mary Butler',089675645,'Peptic Ulcers',Omeprazole 400mg OD, Amoxicillin 500mg TDS,"
#              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer')");
