#select operation to view contents of DOCTOR TABLE
import sqlite3 #imports sqlite3
conn = sqlite3.connect('unit3.db') #opens db
print("Opened database successfully")
cursor = conn.execute("SELECT  DoctorID, FirstName,LastName, Speciality,BleepNo,PHONE from DOCTORS")
print(cursor)
for row in cursor:
    print("DoctorID = ", row[0])
    print("FirstName = ", row[1])
    print("LastName =", row[2])
    print(" Speciality = ", row[3])
    print("BleepNo = ", row[4])
    print("PHONE = ", row[5], "\n")
    print("Operation done successfully")

conn.close() #closes db