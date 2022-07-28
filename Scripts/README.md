  """"""""""27/07/2022"""""""
  
#Today  start working on the Nurses information system.
#This is an information system used by nurses to manage patient information.
#Create a new directory called scripts under the project folder Nurses-Information_system.
#Start by creating an empty directory called templates inside the scripts directory.This will hold all the html files.
#Create a python file called HospitalDb.py under Scripts directory.Start by importing SQLite3 and the use the API 
#conn = sqlite3.connect('unit.db') to connect to unit1.db.Then CREATE TABLE 
#creating table Patient.I Commited changes to git after creating table.
#Noticed i made mistakes while creating the table PATIENT.Deleted HospitalDB.py and unit.db
#I should have started with the doctor table so that i can use doctor id as foreign key in patient table.
#Created hospitalDB.py file and i connected to unit2.db and i just created the doctor's table.
""""""""""""""27/07/22"""""""""""
Created InsertIntoDoctors.py file and transfered the insert statements from HospitalDB.py.Made CreateNursesDb.p and made a nurses table
after importing SQLite3 and using #conn = sqlite3.connect('unit.db'.InsertintoNurses.py is for inserting data into the NURSES 
table while selectNursesdb.py is for selectinf the nurses in the table.CreatePatientDb.py is to create table called PATIENTS
InsertIntoPatient is for inserting data into PATIENT table and selectPatient.py is for selecting
data in patient table.