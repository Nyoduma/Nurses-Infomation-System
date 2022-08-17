#INSERTING DETAILS INTO THE NURSES TABLE
import sqlite3 #imports sqlite3
conn = sqlite3.connect('unit3.db')  #opens database
print("Opened database successfully")
conn.execute("INSERT INTO NURSES (StaffID,FirstName, LastName,  Password,  Level, Mobile,Department,StartDate,Address)\
              VALUES (1,' Tracey', 'More','TM6468', 'CNM1','0870975678','Emergency','2010/01/15','20 The view Drogheda')");
conn.execute("INSERT INTO NURSES (StaffID,FirstName, LastName,  Password,  Level, Mobile,Department,StartDate,Address)\
              VALUES (2,' John', 'Black','@Jnbla', 'Advanced Nurse Practitioner','0850965678','Emergency','2015/01/10','2 The Mills Ardee')");
conn.execute("INSERT INTO NURSES (StaffID,FirstName, LastName,  Password,  Level, Mobile,Department,StartDate,Address)\
              VALUES (3,'Monica', 'Butler','&moniB', 'Junior Nurse','0890966678','Emergency','2021/12/5','18 Park View Skerries')");
conn.execute("INSERT INTO NURSES (StaffID,FirstName, LastName,  Password,  Level, Mobile,Department,StartDate,Address)\
              VALUES (4,' Linda', 'Anyango','nyangi', 'Senior','0850975558','Emergency','2016/01/26','2 The Brew Armah')");
conn.execute("INSERT INTO NURSES (StaffID,FirstName, LastName,  Password,  Level, Mobile,Department,StartDate,Address)\
              VALUES (5,' Rose', 'Burke','@RosyB', 'CNM2','0870973338','Emergency','2009/01/15',' 56 Greenhills Malahide')");
conn.execute("INSERT INTO NURSES (StaffID,FirstName, LastName,  Password,  Level, Mobile,Department,StartDate,Address)\
              VALUES (6,' James', 'Butler','123jmo', 'Junior','0860975778','Emergency','2021/11/15','20 The view Drogheda')");

conn.commit()  #saves data entered in db
print("Records Created Successfully")
conn.close() #closes db
