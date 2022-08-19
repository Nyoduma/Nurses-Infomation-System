#select operation to view contents of NURSES TABLE
import sqlite3 # imports sqlite3
conn = sqlite3.connect('unit3.db') # connects and opens db
print("Opened database successfully")
cursor = conn.execute("SELECT  StaffID,FirstName,LastName,Password,Level,Mobile,Department,StartDate,Email,Address from NURSES")
print(cursor)

for row in cursor:
    print("StaffID = ", row[0])
    print("FirstName = ", row[1])
    print("LastName = ", row[2])
    print("Password =", row[3])
    print(" Level = ", row[4])
    print("Mobile = ", row[5])
    print("Department = ", row[6])
    print("StartDate = ", row[7])
    print("Email = ", row[8])
    print("Address = ", row[9], "\n")

    print("Operation done successfully")

conn.close() #closes db