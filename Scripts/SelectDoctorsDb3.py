#select operation to view contents of DOCTOR TABLE
import sqlite3 #imports sqlite3
conn = sqlite3.connect('unit3.db') #opens db
print("Opened database successfully")
cursor = conn.execute("SELECT  doctorid, first_name,last_name, speciality,bleep_no,phone from doctors")
print(cursor)
for row in cursor:
    print("doctorid = ", row[0])
    print("first_name = ", row[1])
    print("last_name =", row[2])
    print("speciality = ", row[3])
    print("bleep_no = ", row[4])
    print("phone = ", row[5], "\n")
    print("Operation done successfully")

conn.close() #closes db