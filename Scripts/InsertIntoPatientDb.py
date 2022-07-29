#INSERTING DETAILS INTO THE PATIENT TABLE
import sqlite3
conn = sqlite3.connect('unit2.db')
print("Opened database successfully")

conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT,WEIGHT,BMI,BSL,ADDRESS,Mphone, EMAIL,DATEofAdmission,"
              "TIMEOfAdmission,NextOfKin,NextOfKinMobile,CONDITION,CURRENTmeds,NURSINGcare,MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (100, 'James', 'Butler', 32, '175cm', '90kg', 29.4, 4.5, '4 The Park,Ardee,County Louth', 0877798711,'James.butler@gmail.com',"
              "'2022/07/15','09.00hrs', 'Mary Butler', 089675645,'Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
conn.commit()
conn.close()