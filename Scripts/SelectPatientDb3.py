#select operation to view contents of PATIENT TABLE
import sqlite3
conn = sqlite3.connect('unit3.db')
print("Opened database successfully")
cursor = conn.execute("SELECT PatientID,FirstName,SurName,AGE,HEIGHT,WEIGHT,BMI,Mphone,EMAIL,DATEofAdmission,"
                      "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory, Doctor_ID, Staff_ID from PATIENT")
print(cursor)
for row in cursor:
    print("PatientID = ", row[0])
    print("FirstName = ", row[1])
    print("SurName = ", row[2])
    print("AGE = ", row[3])
    print("HEIGHT = ", row[4])
    print("WEIGHT = ", row[5])
    print("BMI  = ", row [6])
    print("Mphone  = ", row[7])
    print("EMAIL  = ", row[8])
    print("DATEofAdmission  = ", row[9])
    print("CONDITION  = ", row[10])
    print("CURRENTmeds  = ", row[11])
    print("NURSINGcare  = ", row[12])
    print("MEDICALhistory  = ", row[13])
    print("Doctor_ID  = ", row[14])
    print("Staff_ID  = ", row[15], "\n") #https://bobbyhadz.com/blog/python-indexerror-tuple-index-out-of-range#:~:text=The%20Python%20%22IndexError%3A%20tuple%20index,len(my_tuple)%20%2D%201%20.
    print("Operation done successfully")
#initially got an error when trying to run the select patient code but googled and got a solution from the above website
conn.close()
