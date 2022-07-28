#select operation to view contents of NURSES TABLE
import sqlite3
conn = sqlite3.connect('unit2.db')
print("Opened database successfully")
cursor = conn.execute("SELECT  StaffID,FirstName,LastName,Level,Mobile,Department,StartDate,Address from NURSES")
print(cursor)
for row in cursor:
    print("StaffID = ", row[0])
    print("FirstName = ", row[1])
    print("LastName = ", row[2])
    print(" Level = ", row[3])
    print("Mobile = ", row[4])
    print("Department = ", row[5])
    print("StartDate = ", row [6])
    print("Address = ", row[7], "\n")
    print("Operation done successfully")

conn.close()