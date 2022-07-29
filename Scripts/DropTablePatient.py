#Create a TABLE
import sqlite3 # imports sqlite3
conn = sqlite3.connect('unit3.db') #opens db
print("Opened database successfully")
conn.execute(" DROP TABLE PATIENT")
conn.close()