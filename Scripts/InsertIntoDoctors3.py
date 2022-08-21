#INSERTING DETAILS INTO THE DOCTORS TABLE
import sqlite3 #imports sqlite3
conn = sqlite3.connect('unit3.db') #opensdb
print("Opened database successfully")
conn.execute("INSERT INTO doctors (doctorid,first_name,last_name, speciality,bleep_no, phone)\
              VALUES (1,' Caroline', 'Amenya', 'Oncology', 130,'0870975678')");

conn.execute("INSERT INTO doctors (doctorid,first_name,last_name, speciality,bleep_no, phone)\
              VALUES (2,' Judy', 'Wambui', 'Dermatology', 101,'0890975667')");
conn.execute("INSERT INTO doctors (doctorid,first_name,last_name, speciality,bleep_no, phone)\
              VALUES (3,' Sarah', 'Liberman', 'Orthopaedics', 1,'0870075678')");
conn.execute("INSERT INTO doctors (doctorid,first_name,last_name, speciality,bleep_no, phone)\
              VALUES (4,'Sandra ', 'Murphy', 'Gynaecology', 13,'0860925478')");
conn.execute("INSERT INTO doctors (doctorid,first_name,last_name, speciality,bleep_no, phone)\
              VALUES (5,' Zack', 'Omondi', 'ortolaryngology', 100,'0870975111')");
conn.execute("INSERT INTO doctors (doctorid,first_name,last_name, speciality,bleep_no, phone)\
              VALUES (6,' James', 'Ajimo', 'Renal', 122,'0898455678')");
conn.execute("INSERT INTO doctors (doctorid,first_name,last_name, speciality,bleep_no, phone)\
              VALUES (7,' Sylvia', 'Anderson', 'Medical', 17,'0850975678')");
conn.execute("INSERT INTO doctors (doctorid,first_name,last_name, speciality,bleep_no, phone)\
              VALUES (8,' Kendra', 'Allando', 'surgical', 150,'0870973331')");
conn.execute("INSERT INTO doctors (doctorid,first_name,last_name, speciality,bleep_no, phone)\
              VALUES (9,' Joseph', 'Butler', 'Cardiology', 16,'0870957896')");
conn.execute("INSERT INTO doctors (doctorid,first_name,last_name, speciality,bleep_no, phone)\
              VALUES (10,' Nathan', 'Butler', 'psychiatry', 155,'0870879578')");

conn.commit() #saves data in db
print("Records Created Successfully")
conn.close() # closes db
