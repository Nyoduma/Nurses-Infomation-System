#select operation to view contents of PATIENT TABLE
import sqlite3
conn = sqlite3.connect('unit2.db')
print("Opened database successfully")
cursor = conn.execute("SELECT PatientID,FirstName,SurName,AGE,HEIGHT,WEIGHT,BMI,BSL,ADDRESS,Mphone,EMAIL,DATEofAdmission,"
                      "TIMEofAdmission, NextOfKin, NextOfKinMobile,CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,"
                      "Doctor_ID,Staff_ID from PATIENT")
print(cursor)
for row in cursor:
    print("PatientID = ", row[0])
    print("FirstName = ", row[1])
    print("SurName = ", row[2])
    print("   AGE = ", row[3])
    print("HEIGHT = ", row[4])
    print("WEIGHT = ", row[5])
    print("BMI  = ", row [6])
    print("BSL = ", row[7])
    print("ADDRESS  = ", row[9])
    print("Mphone  = ", row[10])
    print("EMAIL  = ", row[11])
    print("DATEofAdmission  = ", row[12])
    print("TIMEofAdmission  = ", row[13])
    print("NextOfKin  = ", row[14])
    print(" NextOfKinMobile = ", row[15])
    print("CONDITION  = ", row[16])
    print("CURRENTmeds  = ", row[17])
    print("NURSINGcare  = ", row[18])
    print("MEDICALhistory  = ", row[19])
    print(" Doctor_ID  = ", row[20])
    print(" Staff_ID  = ", row[18], "\n")
    print("Operation done successfully")

conn.close()