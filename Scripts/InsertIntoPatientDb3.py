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
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (103, 'Caro', 'Maeri', 25, '155cm', '68kg', 28.3,' 0891798711','caro.maeri@gmail.com',"
#               "'2022/07/09','Cervical Cancer and Leg ulcer','Solpadein 500mg/8mg/30mg BD, Cisplastin OD',"
#               "'Morning meds administered,Wound dressing done', 'Tuberculosis',1,2)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (104, 'Lucy', 'Hamal', 65, '155cm', '90kg', 37.5,' 0867712311','lucy.hamal@gmail.com',"
#               "'2022/07/19','Obesesity class two,hypercholestrolemia,hypertention','Ramilril 5mg OD,Furosemide 40mg OD, artovastatin 20mg OD',"
#               "'Morning meds administered and patient adviced on low fat diet, good ececise plans to lower weight and manage symptoms', 'Cardiovascular accident 2008',7,5)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (105, 'Ann', 'Sinnot', 18, '170cm', '60kg', 20.8,' 0877000611','ann.sinnot@gmail.com',"
#               "'2022/07/11','Acute Tonsillitis', 'Paracetamol 1gram TDS, Amoxicillin 500mg TDS',"
#               "'Morning meds administered', 'previous ear infection',5,3)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (106, 'Kimmy', 'Sokol', 32, '175cm', '80kg', 26.1,' 0857456711','kimmy.sokol@gmail.com',"
#               "'2022/07/11','Femoral fracture','Difene 75mg OD, Paracetamol 1gm TDS,Nexium 40mg OD',"
#               "'Morning meds administered and assisted patient with toileting', 'previous duodenal ulcer',3,6)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (107, 'Jackie', 'Butler', 62, '155cm', '70kg', 29.1,' 0877798722','jackie.butler@gmail.com',"
#               "'2022/07/11', 'Diabetes Mellitus', 'Glucophage 100mg BD', 'Vitals checked and recorded. Medication administered',"
#               "'Pneumonia', 8, 6)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (108, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
              "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (109, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
              "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (110, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
              "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (111, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
              "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (112, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (113, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
#               "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
#               "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
# conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
#               "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
#               VALUES (114, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
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
