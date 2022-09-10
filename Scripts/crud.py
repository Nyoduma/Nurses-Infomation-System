from flask import *  #this imports everything from the flask module
import sqlite3  # This imports sqlite3

app = Flask(__name__,template_folder='templates')





#LOGIN
@app.route('/', methods=["POST", "GET"])
def loging():
    msg=""

    if request.method == "POST":
        # Connect to db
        con = sqlite3.connect("unit3.db")
        cur = con.cursor()
        #HTML Form
        email = request.form['email']
        password = request.form['password']
        #Querry
        cur.execute("SELECT * FROM nurses WHERE  email='"+email+"' AND password= '"+password+"'")
        info = cur.fetchall()
        if info:
            return redirect(url_for('kazi'))
        else:


            msg = "Invalid username or password.Please try again"

    return render_template('login.html', msg=msg)




#REGISTER
@app.route('/register', methods=["POST", "GET"])
def register():
    msg = ""


    if request.method == "POST":

        try:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            password = request.form['password']
            level = request.form['level']
            mobile = request.form['mobile']
            department = request.form['department']
            start_date = request.form['start_date']
            email = request.form['email']
            address = request.form['address']
            with sqlite3.connect("unit3.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO nurses(first_name,last_name,password,level,"
                            "mobile, department, start_date, email,address) VALUES (?,?,?,?,?,?,?,?,?)",
                            (first_name, last_name, password, level, mobile, department,
                             start_date, email, address))
                con.commit()

        except Exception as e:  # taken from: https://pythonprogramming.net/flask-error-handling-basics/
            con.rollback()
            msg = str(e)
            # check for email error

            if msg == 'UNIQUE constraint failed: nurses.email':
                email_error = 'Email in use, please enter a new email'
                return render_template('register.html', email_error=email_error)
            #Check any other error
            else:
                msg = "We cannot add nurse to the list because:{}".format(e)
                return render_template('register.html', msg=msg)
        finally:
            if msg == 'UNIQUE constraint failed: nurses.email':
                email_error = 'Email in use, please enter a new email'
                return render_template('register.html', email_error=email_error)
                # Check any other error
            else:
                return redirect(url_for('loging'))

            con.close()

    return render_template('register.html', msg=msg)




@app.route('/duties')
def kazi():
    return render_template('duties.html')

@app.route('/add')
def creating():
    return render_template('add.html')

#CREATE PATIENT
@app.route('/save', methods=["POST", "GET"])
def save():

    msg = ""
    if request.method == "POST":
        try:
            patient_id = request.form["patient_id"]
            first_name = request.form["first_name"]
            sir_name = request.form["sir_name"]
            age = request.form["age"]
            height = request.form["height"]
            weight = request.form["weight"]
            bmi = request.form["bmi"]
            mobile_phone = request.form["mobile_phone"]
            email = request.form["email"]
            date_of_admission = request.form["date_of_admission"]
            condition = request.form["condition"]
            current_meds = request.form["current_meds"]
            nursing_care = request.form["nursing_care"]
            medical_history = request.form["medical_history"]
            doctor_id = request.form["doctor_id"]
            staff_id = request.form["staff_id"]



            with sqlite3.connect("unit3.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into patient (patient_id,first_name,sir_name,age,height,weight,bmi,mobile_phone,"
                            "email,date_of_admission, condition, current_meds,nursing_care,medical_history,doctor_id,"
                            "staff_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                            (patient_id, first_name, sir_name, age, height, weight, bmi, mobile_phone,
                             email, date_of_admission, condition, current_meds, nursing_care, medical_history,
                             doctor_id, staff_id))
                con.commit()
                msg = "Patient successfully Added"
        except Exception as e:  # taken from: https://pythonprogramming.net/flask-error-handling-basics/
            con.rollback()
            msg = str(e)
            msg = "We cannot add the patient to the list because of:{} Please enter details in full". format(e)
        finally:
            return render_template("success.html", msg=msg)
            con.close()



#VIEW PATIENTS

@app.route('/view')
def view():
    con = sqlite3.connect("unit3.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from patient ")
    rows = cur.fetchall()
    return render_template('view.html', rows=rows)

#VIEW FOR DOCTORS
@app.route('/view_doctors')
def view_doctors():
    con = sqlite3.connect("unit3.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from doctors ")
    rows = cur.fetchall()
    return render_template('viewDocs.html', rows=rows)


#VIEW CONDITIONS
@app.route('/view_conditions')
def view_conditions():
    con = sqlite3.connect("unit3.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT patient_id, condition from patient ")
    rows = cur.fetchall()
    return render_template('viewConditions.html', rows=rows)


#UPDATE
@app.route('/update/<int:pid>', methods=["POST", "GET"])
def update(pid):
    #connectiong to database and setting up the cursor
    con = sqlite3.connect("unit3.db")
    cur = con.cursor()
    msg = ""  #initialising the msg variable


    if request.method == 'GET': # get the information from the database based on user id
        try:
            con.row_factory = sqlite3.Row
            cur.execute("SELECT * FROM  patient where patient_id = ?", [pid])
            patient_info = cur.fetchone() #set the information received from database
            con.close()

        except Exception as e:  # taken from: https://pythonprogramming.net/flask-error-handling-basics/
            con.rollback()
            msg = str(e)

        finally:
            return render_template('update.html', patient_info=patient_info,  msg=msg) #pass information to update.html to be prepopulated into the html form.


    if request.method == 'POST':    #updating patient data

        try:
            first_name = request.form["first_name"]
            sir_name = request.form["sir_name"]
            age = request.form["age"]
            height = request.form["height"]
            weight = request.form["weight"]
            bmi = request.form["bmi"]
            mobile_phone = request.form["mobile_phone"]
            email = request.form["email"]
            date_of_admission = request.form["date_of_admission"]
            condition = request.form["condition"]
            current_meds = request.form["current_meds"]
            nursing_care = request.form["nursing_care"]
            medical_history = request.form["medical_history"]
            doctor_id = request.form["doctor_id"]
            staff_id = request.form["staff_id"]

            cur.execute("UPDATE patient SET first_name = ?,sir_name = ?,age = ?,height = ?,weight = ?,bmi = ?,mobile_phone = ?,"
                            "email = ?,date_of_admission = ?, condition= ?, current_meds = ?,nursing_care = ?,medical_history = ?,doctor_id = ?,"
                            "staff_id = ? WHERE patient_id = ?", (first_name, sir_name, age, height, weight, bmi, mobile_phone,
                             email, date_of_admission, condition, current_meds, nursing_care, medical_history,
                             doctor_id, staff_id, pid))
            con.commit()
            con.close()
            msg = "Patient successfully Updated"

        except Exception as e:  # taken from: https://pythonprogramming.net/flask-error-handling-basics/
            con.rollback()
            msg = str(e)
            msg = "We cannot update the patient to the list because of:{}".format(e)

        finally:
            return redirect(url_for('kazi', msg=msg))





@app.route('/delete_record/<int:pid>')
def delete_record(pid):
    msg = ""


    with sqlite3.connect("unit3.db") as con:  # connect to db
        try:
            cur = con.cursor()
            cur.execute("delete from patient where patient_id = ?", (pid,))
            con.commit()
            msg = "record successfully deleted"
        except Exception as e:  #taken from:  https://pythonprogramming.net/flask-error-handling-basics/
            con.rollback()
            msg = str(e)
            msg = "can't be deleted because: {}".format(e)
        finally:

            return redirect(url_for('kazi', msg=msg))
            con.close()





if __name__=='__main__':
    app.run(host='0.0.0.0',port='8080',debug=True)   # taken from: https://replit.com/talk/ask/Flask-app-doesnt-load-in-the-browser-need-help/116192
