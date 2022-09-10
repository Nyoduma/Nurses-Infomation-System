  """"""""""27/07/2022 is the initiation phase""""""
  
To recreate this project, first download pycharm and python into your pc.Open pycharm and make a new project.Download flask and sqlite3 into your environment
Start by creating an sqlite3 database by opening three.py files namely: 
CreateDoctorsDb3.py,CreateNursesDb3.py and CreatPatientDb3.py and start typing the below code:
import sqlite3  # this imports sqlite3
conn = sqlite3.connect('unit3.db)  # this opens the database
conn.execute('''create table table name (add values);''') to create table for doctors, nurses and patient.
conn.close() # to close the database each time you open the database.

To insert information into the tables open three different .py files inside scripts namely;InsertIntoDoctors3.py,
InsertIntoNursesDb3.py and InsertIntoPatientDb3.py and in each .py file run the below code:
import sqlite3 #imports sqlite3
conn = sqlite3.connect('unit3.db') #opensdb
print("Opened database successfully")
conn.execute("INSERT INTO table name ()  VALUES ()");
conn.commit() #saves data in db
print("Records Created Successfully")
conn.close() # make sure to close the db each time 
do this for patient table,doctors table and nurses table and add values.

To be able to see information in the database, open three separate.py files inside scripts
namely; SelectDoctorsDb3.py, Select NursesDb3.py and SelectPatientDB3.py and insert three separate codes into each .py file foer
the nurses table,doctors table and patient table as follows:

import sqlite3 #imports sqlite3
conn = sqlite3.connect('unit3.db') #opens db
print("Opened database successfully")
cursor = conn.execute("SELECT  table name, values FROM table name")
print(cursor)
for row in cursor:
    print(" insert your values as per table= ", row[0])
    print("Operation done successfully")
     conn.close() #closes db

For droping the tables,create three different .py files namely DropTablrDoctors.py,DropTableNurses.py and 
DropTablePatient.py and type the below code on each file but specify the table name as follows:
import sqlite3 # imports sqlite3
conn = sqlite3.connect('unit3.db') #opens db
print("Opened database successfully")
conn.execute(" DROP TABLE table name")
conn.close()

Open another .py file under scripts and name it as crud.py where you will do all the crud operations.
open a new directory under scripts and name it as templates and in templates open the following html files:
add.html- for adding patient
base.html - static page that has jinja2 syntax that reflects on all other pages except login and register .html
duties.html- which is the homepage
login.html -  creates interface for loging nurses in
register.html - for registering patients
success.html - to inform nurse that patient has been successfully added
update.html- to pre-populate patient information during an update 
view.html- for viewing patient records
viewConditions.html- for viewing patient id and conditions
viewDocs.html- for viewing a list of doctors

You will need to create a static directory under scripts and here you can create another directory and name 
it css and inside css make a file called main.css and add css code to it.This css file will be liked in 
base.html as follows:
<link rel="stylesheet" href="{{url_for('static', filename='css/main.css') }}">
on the base.html add another css link for tailwind css as follows:
  <script src="https://cdn.tailwindcss.com"></script>
add the below code as well:
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

for debugging the crud set the following code at the bottom

if __name__=='__main__':
    app.run(host='0.0.0.0',port='8080',debug=True) 
