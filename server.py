""" Appointment Scheduling and Confirmation""" 

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, session, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db,db, Patient,Appointment, AppointmentType, BusinessOwner
from database_functions import create_new_pt, create_new_appt, create_appt_type, create_new_owner
from datetime import datetime,timedelta
app = Flask(__name__)

app.secret_key = "ABC"
# source this later

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
	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")
	date_of_birth = request.form.get("date_of_birth")
	cell_phone_number = request.form.get("cell_phone_number")
	user_name = request.form.get("user_name")
	password = request.form.get("password")
	# user_id= request.form["user_id"]


	patient = create_new_pt(first_name=first_name, 
							last_name=last_name, 
							date_of_birth=date_of_birth, 
							cell_phone_number=cell_phone_number, 
							user_name=user_name,
							password=password)

	session['first_name'] = first_name 

	db.session.add(patient)
	db.session.commit()

	time_now= datetime.now()
	td= timedelta(1)

	first_available_day = time_now + td 
	weekdays= ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
	for day in weekdays:
		if day in weekdays:
			first_available_day= time_now +td
		else: 
			first_available_day= time_now +timedelta(3)

	day=first_available_day.day
	month=first_available_day.month
	year=first_available_day.year
	
	return render_template("appt_book.html", day=day, year=year, month=month)

@app.route('/existing_user_login', methods=['GET'])
def show_options_for_user():
	""" show existing user a page to choose from two options"""
	
	user_name=request.args.get('user_name')
	password= request.args.get('password')
	
	session['user_name']= user_name
	
	patient= Patient.query.filter_by(user_name=user_name).first

	return redirect('existing_user_page.html')

@app.route('/login', methods=['POST'])
def show_appts_scheduled_for_this_pt():
	""" show the user all the appointments that he/she has scheduled"""
	
	user_name= request.form.get('user_name')
	password=request.form.get('password')
	print user_name
	patient = Patient.query.filter_by(user_name=user_name).first()
	print patient
	first_name = patient.first_name
	
	# patient_id= patient.user_id

	# all_appts = Appointment.query.filter_by(user_id=patient_id).all()
	# print all_appts

	if patient.password == password:
		user_id= patient.user_id
		session['user_id']= user_id

		return render_template("existing_user_page.html", first_name=first_name)
	else:
		flash("Please enter the correct password!")
		return redirect ('plogin')


@app.route('/reviews/', methods=['GET'])
def show_review_page():
	"""Display reviews page"""

	return render_template("eviews.html")

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
def show_appt_book():
	"""This will take the pts name and show the appt book"""
	first_name= request.args.get('first_name')
	# year="2016"
	# month="August"
	# day="1"
	time_now= datetime.now()
	td= timedelta(1)

	first_available_day = time_now + td 
	weekdays= ['Monday','Tuesday','Wednesday','Thursday',]
	for day in weekdays:
		if day in weekdays:
			first_available_day= time_now +td
		else: 
			first_available_day= time_now +timedelta(3)
		#get a code review for the above!!
	day=first_available_day.day
	month=first_available_day.month
	year=first_available_day.year
	print day 
	print month 
	print year
	appointments = {}

	return render_template ("appt_book.html", first_name=first_name, day=day, year=year, month=month)


@app.route ('/appt_book/<year>/<month>/<day>', methods=['POST'])
def appt_book_view(year,month,day):
	"""Appointment book view"""
	time_now= datetime.now()
	td= timedelta(1)

	first_available_day = time_now + td 
	weekdays= [Monday, Tuesday, Wednesday, Thursday,]
	for day in weekdays:
		if day in weekdays:
			first_available_day= time_now +td
		else: 
			first_available_day= time_now +timedelta(3)
		#get a code review for the above!!
	day=first_available_day.day
	month=first_available_day.month
	year=first_available_day.year
	print day 
	print month 
	print year
	appointments = {}

	return render_template("appt_book.html", year=year, month=month, day=day, appointments=appointments)

@app.route ('/confirm_appt', methods=['GET'])
def show_scheduled_appts():
	""" Display page to show what is scheduled for this user"""
	user_id= session.get('user_id')
	patient = Patient.query.filter_by(user_id=user_id).first()
	first_name = patient.first_name
	appointments= Appointment.query.filter_by(user_id=user_id).all()
	

	return render_template("/confirmed.html",first_name=first_name,appointments=appointments)

@app.route ('/confirm_appt', methods=['POST'])
def conf_appt():
	""" Need to send user to another page after appt has been confirmed"""

	appt_time = request.form.get('appt_time')
	provider_id, time = appt_time.split(", ")
	first_name = session['first_name']

	patient = Patient.query.filter_by(first_name=first_name).first()
	user_id =patient.user_id 
	
	created_appt= create_new_appt(user_id=user_id,
							appt_type_id=1,
							appt_time=time,
							provider_id=provider_id)
	
	db.session.add(created_appt)
	db.session.commit()

	appointments= Appointment.query.filter_by(user_id=user_id).all()

	return render_template("confirmed.html",first_name=first_name, appointments=appointments)

# TODO: Make /confirm_appt route for [get] - this shows all appointments for user

if __name__ == "__main__":
	
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')





