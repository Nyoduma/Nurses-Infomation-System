#INSERTING DETAILS INTO THE NURSES TABLE
import sqlite3 #imports sqlite3
conn = sqlite3.connect('unit3.db')  #opens database
print("Opened database successfully")
conn.execute("INSERT INTO nurses (staffid,first_name, last_name,  password,  level, mobile,department,start_date,email,address)\
              VALUES (1,' Tracey', 'More','TM6468', 'Clinical Nurse Manager(CNM) 1','0870975678','Emergency','2010/01/15','tracey.more@yahoo.com','20 The view Drogheda')");
conn.execute("INSERT INTO NURSES (staffid,first_name, last_name,  password,  level, mobile,department,start_date,email,address)\
              VALUES (2,' John', 'Black','@Jnbla', 'Advanced Nurse Practitioner','0850965678','Emergency','2015/01/10','john.black22@yahoo.com','2 The Mills Ardee')");
conn.execute("INSERT INTO NURSES (staffid,first_name, last_name,  password,  level, mobile,department,start_date,email,address)\
              VALUES (3,'Monica', 'Butler','&moniB', 'Junior Nurse','0890966678','Emergency','2021/12/5','monica.butler@gmail.com','18 Park View Skerries')");
conn.execute("INSERT INTO NURSES (staffid,first_name, last_name,  password,  level, mobile,department,start_date, email, address)\
              VALUES (4,' Linda', 'Anyango','nyangi', 'Senior Nurse','0850975558','Emergency','2016/01/26','linda.anyango@gmail.com','2 The Brew Armah')");
conn.execute("INSERT INTO NURSES (staffid,first_name, last_name,  password,  level, mobile,department,start_date, email, address)\
              VALUES (5,' Rose', 'Burke','@RosyB', 'Clinical Nurse Manager(CNM) 2','0870973338','Emergency','2009/01/15','rose.burke11@yahoo.com', '56 Greenhills Malahide')");
conn.execute("INSERT INTO NURSES (staffid,first_name, last_name,  password,  level, mobile,department,start_date, email, address)\
              VALUES (6,' James', 'Butler','123jmo', 'Junior Nurse','0860975778','Emergency','2021/11/15','james.butler@gmail.com','20 The view Drogheda')");

conn.commit()  #saves data entered in db
print("Records Created Successfully")
conn.close() #closes db
