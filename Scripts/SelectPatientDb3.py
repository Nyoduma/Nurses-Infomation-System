#select operation to view contents of PATIENT TABLE
import sqlite3
conn = sqlite3.connect('unit3.db')
print("Opened database successfully")
cursor = conn.execute("SELECT patient_id,first_name,sir_name, age,height,weight,bmi,mobile_phone,email,date_of_admission,"
                      "condition, current_meds, nursing_care, medical_history, doctor_id,  staff_id from patient")
print(cursor)
for row in cursor:
    print("patient_id = ", row[0])
    print("first_name = ", row[1])
    print("sir_name = ", row[2])
    print("age = ", row[3])
    print("height = ", row[4])
    print("weight = ", row[5])
    print("bmi  = ", row [6])
    print("mobile_phone  = ", row[7])
    print("email  = ", row[8])
    print("date_of_admission  = ", row[9])
    print("condition  = ", row[10])
    print("current_meds  = ", row[11])
    print("nursing_care  = ", row[12])
    print("medical_history  = ", row[13])
    print("doctor_id  = ", row[14])
    print("staff_id = ", row[15], "\n") #https://bobbyhadz.com/blog/python-indexerror-tuple-index-out-of-range#:~:text=The%20Python%20%22IndexError%3A%20tuple%20index,len(my_tuple)%20%2D%201%20.
    print("Operation done successfully")
#initially got an error when trying to run the select patient code but googled and got a solution from the above website
conn.close()
