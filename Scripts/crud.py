

from flask import *  #this imports everything from the flask module
import sqlite3  # This imports sqlite3

app = Flask(__name__,template_folder='templates')





@app.route('/', methods=["POST", "GET"])
def loging():
    if request.method == "POST":
        #Connect to db
        con = sqlite3.connect("unit3.db")
        cur = con.cursor()
        #HTML Form
        email = request.form['email']
        password = request.form['password']
        #Querry
        cur.execute("SELECT * FROM nurses WHERE  email='"+email+"' AND password= '"+password+"'")
        info = cur.fetchall()
        if len(info) == 0:
            print("Incorrect credentials entered.Please try again")

        else:
            return redirect(url_for('kazi'))
    return render_template('login.html')


@app.route('/duties')
def kazi():
    return render_template('duties.html')

@app.route('/add')
def creating():
    return render_template('add.html')


@app.route('/save', methods=["POST", "GET"])
def save():

    msg = "msg"
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
            msg = "We cannot add the patient to the list because of:", format(e)
        finally:
            return render_template("success.html", msg=msg)
            con.close()




@app.route('/view')
def view():
    con = sqlite3.connect("unit3.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from patient ")
    rows = cur.fetchall()
    return render_template('view.html', rows=rows)

@app.route('/delete')
def delete():
    return render_template("delete.html")


@app.route('/deleterecord', methods=["POST"])
def deleterecord():
    patient_id = request.form["patient_id"]
    with sqlite3.connect("unit3.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from patient where patient_id = ?", patient_id)
            msg = "record successfully deleted"
        except Exception as e:  # https://pythonprogramming.net/flask-error-handling-basics/
            con.rollback()
            msg = str(e)
            msg = "can't be deleted because:",format(e)
        finally:
            return render_template("delete_record.html", msg=msg)













if __name__=='__main__':
    app.run(host='0.0.0.0',port='8080',debug=True)   # taken from: https://replit.com/talk/ask/Flask-app-doesnt-load-in-the-browser-need-help/116192
