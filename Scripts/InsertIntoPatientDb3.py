#INSERTING DETAILS INTO THE PATIENT TABLE
import sqlite3
conn = sqlite3.connect('unit3.db')
print("Opened database successfully")

# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (101, 'Richard', 'Butler', 45, '182cm', '50kg', 17.8,' 0857722711','richard.butler@gmail.com',"
#               "'2022/07/11','Prostate Cancer','Apalutamide 400mg OD, Cabazitaxel 500mg TDS',"
#               "'Morning meds administered,Patient assisted with bathing', 'pneumonia,gout', 1,2)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (102, 'Mary', 'Black', 32, '175cm', '90kg', 29.4,'0851798711','mary.black@gmail.com',"
#               "'2022/07/12','Pelvic Inflamatory Disease','Flagyl 400mg TDS, Amoxicillin 500mg TDS,Diclofenac 75mg OD',"
#               "'Morning meds administered', 'previous Pelvis Inflammatory Disease(PID), Bacterial vaginosis',4,5)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
              "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
              "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
              "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
              "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
              "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
              "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
              "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
              "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
              "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
              "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
              "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
              "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
# v
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
# v
# v
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
#
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
#
#
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");

conn.commit()
conn.close()
