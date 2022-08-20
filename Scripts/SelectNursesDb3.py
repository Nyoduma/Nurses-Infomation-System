#select operation to view contents of NURSES TABLE
import sqlite3 # imports sqlite3
conn = sqlite3.connect('unit3.db') # connects and opens db
print("Opened database successfully")
cursor = conn.execute("SELECT  staffid, first_name, last_name,password,level,mobile,department,start_date,email,address from nurses")
print(cursor)

for row in cursor:
    print("staffid = ", row[0])
    print("first_name = ", row[1])
    print("last_name = ", row[2])
    print("password =", row[3])
    print(" level = ", row[4])
    print("mobile = ", row[5])
    print("department = ", row[6])
    print("startDate = ", row[7])
    print("email = ", row[8])
    print("address = ", row[9], "\n")

    print("Operation done successfully")

conn.close() #closes db