#INSERTING DETAILS INTO THE PATIENT TABLE
import sqlite3
conn = sqlite3.connect('unit3.db')
print("Opened database successfully")

conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (100, 'Paul', 'Butler', 32, '175cm', '90kg', 29.4,' 0877798711','paul.butler@gmail.com',"
              "'2022/07/15','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'previous duodenal ulcer',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (101, 'Richard', 'Butler', 45, '182cm', '50kg', 17.8,' 0857722711','richard.butler@gmail.com',"
              "'2022/07/11','Prostate Cancer','Apalutamide 400mg OD, Cabazitaxel 500mg TDS',"
              "'Morning meds administered,Patient assisted with bathing', 'pneumonia,gout', 1,2)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (102, 'Mary', 'Black', 32, '175cm', '90kg', 29.4,'0851798711','mary.black@gmail.com',"
              "'2022/07/12','Pelvic Inflamatory Disease','Flagyl 400mg TDS, Amoxicillin 500mg TDS,Diclofenac 75mg OD',"
              "'Morning meds administered', 'previous Pelvis Inflammatory Disease(PID), Bacterial vaginosis',4,5)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (103, 'Caro', 'Maeri', 25, '155cm', '68kg', 28.3,' 0891798711','caro.maeri@gmail.com',"
              "'2022/07/09','Cervical Cancer and Leg ulcer','Solpadein 500mg/8mg/30mg BD, Cisplastin OD',"
              "'Morning meds administered,Wound dressing done', 'Tuberculosis',1,2)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (104, 'Lucy', 'Hamal', 65, '155cm', '90kg', 37.5,' 0867712311','lucy.hamal@gmail.com',"
              "'2022/07/19','Obesesity class two,hypercholestrolemia,hypertention','Ramilril 5mg OD,Furosemide 40mg OD, artovastatin 20mg OD',"
              "'Morning meds administered and patient adviced on low fat diet, good ececise plans to lower weight and manage symptoms', 'Cardiovascular accident 2008',7,5)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (105, 'Ann', 'Sinnot', 18, '170cm', '60kg', 20.8,' 0877000611','ann.sinnot@gmail.com',"
              "'2022/07/11','Acute Tonsillitis', 'Paracetamol 1gram TDS, Amoxicillin 500mg TDS',"
              "'Morning meds administered', 'previous ear infection',5,3)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (106, 'Kimmy', 'Sokol', 32, '175cm', '80kg', 26.1,' 0857456711','kimmy.sokol@gmail.com',"
              "'2022/07/11','Femoral fracture','Difene 75mg OD, Paracetamol 1gm TDS,Nexium 40mg OD',"
              "'Morning meds administered and assisted patient with toileting', 'previous duodenal ulcer',3,6)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (107, 'Jackie', 'Butler', 62, '155cm', '70kg', 29.1,' 0877798722','jackie.butler@gmail.com',"
              "'2022/07/11', 'Diabetes Mellitus', 'Glucophage 100mg BD', 'Vitals checked and recorded. Medication administered',"
              "'Pneumonia', 8, 6)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (108,'Macy', 'Lins', 40, '152cm', '70kg', 30.3,' 0857700711','macy.lins@gmail.com',"
              "'2022/07/15','Tonsillitis','CO_Amoxiclav 500mg/125mg TDS * 5/7, Paracetamol 1gm OD * 3/7',"
              "'Morning meds administered, Reasssurance given', 'Migraine',5,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (109, 'Moses', 'Black', 32, '155cm', '60kg', 25.0,' 0871230711','moses.black@gmail.com',"
              "'2022/07/14','hernia','Omeprazole 400mg OD * 10/7', 'Morning meds administered and patient adviced on good diet to manage symptoms',"
             "'previous duodenal ulcer',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (110, 'Erick', 'Junior', 70, '175cm', '90kg', 29.4,' 0857798700','erick.junior@gmail.com',"
              "'2022/07/10','CVA','artovastatin 75 mg OD,Aspirin 300mgTenecteplase 40mg OD',"
              "'Morning meds administered,repositioned patient regularly', 'depression,chain smoker',9,1)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (111, 'Christine', 'Murphy', 25, '165cm', '70kg', 25.7,' 0837798711','christine.murphy@gmail.com',"
              "'2022/07/15','Major depression,Attempted suicide','Paroxetin 20mg BD, ',"
              "'Morning meds administered and coucelling done,Doctor contacted', 'Depression',10,1)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (112, 'Monica', 'Mugambi', 24, '175cm', '50kg', 16.3,' 0837908711','monica.mugambi@gmail.com',"
              "'2022/07/10','Asthma','Pulmicort nebulization 20mg TDS,Adrenalin 0.5mg OD',"
              "'Morning meds administered,Nebulisation done and patient adviced on good diet to manage symptoms', 'previous asthmatic attack',7,1)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (113, 'Cynthia', 'Bray', 66, '145cm', '70kg', 29.4,' 0866695711','cynthia.bray@gmail.com',"
              "'2022/07/10','Cervical Cancer','pembrolizumab 200mg  iv over 30mins, paracetamol 1gram TDS',"
              "'Morning meds administered','athma,dysmenhoria',1,2)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (114, 'Lynn', 'Ngugi', 42, '155cm', '60kg', 25,'0857793331','lynn.ngugi@gmail.com',"
              "'2022/07/11','Schizophrenia','Largactil 1gram', 'Medication given and councelling done',"
              "'Bipollar',10,1)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (115, 'James', 'Sinnot', 35, '175cm', '80kg', 26.1, '0877798711', 'james.sinnot@gmail.com',"
              "'2022/07/09','Adenoiditis','paracetamil 1gm TDS, Amoxicillin 500mg TDS',"
              "'Morning meds administered', ' pneumonia',5,5)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (116, 'Samuel', 'Tayong', 28, '171cm', '60kg', 20.5,' 0827798711','samuel.tayong@gmail.com',"
              "'2022/07/12','Facture tibia','Difene 75mg OD, Paracetamol !gm TDS ,Amoxicillin 500mg TDS',"
              "'Morning meds administered and Doctor bleeped,Vital signs checked and are within normal range','Facture wrist',3,5)");

conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (117, 'Esther', 'ologunola', 42, '155cm', '70kg', 22.3,' 0837123711','esther.ologunola@gmail.com',"
              "'2022/07/10','chronic constipation','movicol two satchets TDS, two senna nocte',"
              "'Morning meds administered and patient encouraged to drink plenty fluids and eat more roughage to manage symptoms', 'anal fissure',8,5)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (118, 'Mary', 'Jude', 31, '165cm', '60kg', 22.0,' 0837798331','mary.jude@gmail.com',"
              "'2022/07/09','chronic  ulcerated wound','Azythromycinnone tabs OD * 3/7, Ibuprofen 400mg TDS',"
              "'Morning meds administered and wound dressing done', 'Duodenal ulcer',8,3)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (119, 'Carmen', 'Rakauskas', 70, '155cm', '90kg', 37.2,' 0827789711','carmen.rakauskas@gmail.com',"
              "'2022/07/13', 'Hypertention, hepercholestolemia', ' captoptril 25mg OD',"
              "'Patient adviced on reducing salt and trans fats in diet ,Morning meds administered ,blood pressured and is very .Doctor bleeped ',"
             " 'Duodenal Ulcer',9,3)");


conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (120, 'Paul', 'Aseko', 50, '175cm', '90kg', 29.4,' 0820098711','paul.aseko@gmail.com',"
              "'2022/07/14','Urinary Tract Infection,Kidney stones,Phemosis', 'Amoxicillin 500mg TDS * 7/7,Iburofen 400mg',"
              "'Morning meds administered and patient adviced to drink plenty fluids', 'Gout',6,2)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (121, 'Michael', 'Tayong', 32, '155cm', '70kg', 22.3,' 0817798711','michael.tayong@gmail.com',"
              "'2022/07/09','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'Alopecia, Appendicitis',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (122, 'Paul', 'Butler', 60, '175cm', '90kg', 29.4,' 0855798711','paul777.butler@gmail.com',"
              "'2022/07/12','Generalised skin rash','Tetracyclin apply TDS',"
              "'Morning meds administered ', 'Boils',2,3)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (123, 'Cynthia', 'Butler', 72, '165cm', '60kg', 22.0,' 0847798701','cynthia.butler@gmail.com',"
              "'2022/07/15','Dyhydration in Dementia','I.V Normal 100mls saline to run slowly over 24hrs',"
              "'Monitoring I.V fluids,frequently checkind vital signs,reassurance given', 'Hernia,Pneumonia',10,6)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (124, 'James', 'Ajimo', 68, '175cm', '90kg', 29.4,' 0847689891','james.ajimo@gmail.com',"
              "'2022/07/12','Ankle oedema,hypertention','Captoptril 5mg OD, Furosemide 40mgBD',"
              "'Morning meds administered and patient ,BP checked and high same documented,Doctor informed', 'Adenoiditis',7,6)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (125, 'sussie', 'Wanjiru', 20, '155cm', '50kg', 20.8,' 0887798711','sussie.wanjiru@gmail.com',"
              "'2022/07/10','Peptic Ulcers','Omeprazole 400mg OD, Amoxicillin 500mg TDS',"
              "'Morning meds administered and patient adviced on good diet to manage symptoms', 'Pneumonia',8,4)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (126, 'Barry', 'Burke', 29, '175cm', '90kg', 29.4,' 0880098711','garry.burke@gmail.com',"
              "'2022/07/10','Migraine','Difene 75mg TDS,paracetamol 1gram TDS',"
              "' meds administered and transferred patient into a dark room to prevent photosensitivity', 'Recurrent ear infections',7,6)");
conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (127, 'Lucy', 'Shannon', 32, '170cm', '60kg', 20.8,' 0887792211','lucy.shannon@gmail.com',"
              "'2022/07/09','70% Burns','Solpadein dissolvable 2 Tablets  TDS, Amoxicillin 500mg TDS','Medication given as prescribed ,Dressing done',"
             " 'Depression',7,6)");

conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (128, 'Magda', 'Laton', 44, '175cm', '90kg', 29.4,' 0857724611','magda.laton@yahoo.com',"
              "'2022/07/11','Nephritis','Ciprofoxacin 500mg TDS, ibuprofen 400mg TDS',"
              "'Medication administered and Rennal Doctor bleeped', 'previous duodenal ulcer',6,3)");


conn.execute("INSERT INTO PATIENT (PatientID,FirstName, SurName,AGE, HEIGHT, WEIGHT,BMI,Mphone, EMAIL,DATEofAdmission,"
              "CONDITION, CURRENTmeds, NURSINGcare, MEDICALhistory,Doctor_ID, Staff_ID)\
              VALUES (129, 'Denise', 'Sinnot', 42, '168cm', '70kg', 24.8,' 0817008711','dennise.sinnot@hotmail.com',"
              "'2022/07/13','threatened miscarriage','paracetamol 1gm TDS ',"
              "'Medication administered and reassurance given.Vital signs monitored', 'dysmenorrhea',4,2)");

conn.commit()
conn.close()
