""" Appointment Scheduling and Confirmation""" 

from jinja2 import StrictUndefined
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db,db
from database_functions import create_new_pt, create_new_appt, create_appt_type, create_new_owner

app = Flask(__name__)

app.secret_key = "ABC"

#this line is so jinja will show an error if a variable is used but undefined.
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
	""" This is the homepage"""

	return render_template("homepage.html")

@app.route('/plogin', methods=['GET'])
def login():
	"""This will allow the business owner and patient to log in. Show the forms"""

	return render_template("pt_login_form.html")

@app.route('/pregister', methods=['POST'])
def login_process():
	"""Process login"""
	#Getting the variables
	first_name = request.form["first_name"]
	last_name = request.form["last_name"]
	date_of_birth = request.form["date_of_birth"]
	cell_phone_number = request.form["cell_phone_number"]
	user_name = request.form["user_name"]
	password = request.form["password"]
	# user_id= request.form["user_id"]


	patient = create_new_pt(first_name=first_name, 
							last_name=last_name, 
							date_of_birth=date_of_birth, 
							cell_phone_number=cell_phone_number, 
							user_name=user_name,
							password=password)

	# #this part might need to change. Need to figure out how to add a pt into the database
	if not patient:
		flash("Please complete the new patient form!")
		return redirect ("/pregister")

	if patient.password != password:
		flash("Incorrect password")
		return redirect ("/login")
# query the appt table for times that are today. 
#look at ratigs 
	return render_template("appt_book.html")

@app.route('/reviews', methods=['GET'])
def show_review_page():
	"""Display reviews page"""

	return render_template("reviews.html")

@app.route('/owner_login', methods=['GET'])
def owner_page():
	"""Display form for owner"""

	return render_template("owner_login.html")

@app.route('/owner_login', methods=['POST'])
def owner_login_process():
	"""Process owner login"""

	"""Process owner login"""
	first_name=request.form["first_name"]
	last_name=request.form["last_name"]
	license_number=request.form["license_number"]
	office_address=request.form["office_address"]
	office_phone_number=request.form["office_phone_number"]
	provider_id=request.form["provider_id"]

	new_owner= create_new_owner(first_name=first_name,
								last_name=last_name,
								license_number=license_number,
								office_address=office_address,
								office_phone_number=office_phone_number,
								 provider_id=provider_id )

	db.session.add(new_owner)
	db.session.commit()

	return render_template("appt_book.html")

@app.route ('/appt_book', methods=['GET'])
def appt_book_view():
	"""Appointment book view"""

	return render_template("appt_book.html")

if __name__ == "__main__":
	
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')





