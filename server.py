""" Appointment Scheduling and Confirmation""" 

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, session
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

	session['first_name'] = first_name 

	# #this part might need to change. Need to figure out how to add a pt into the database
	if not patient:
		flash("Please complete the new patient form!")
		return redirect ("/pregister")

	if patient.password != password:
		flash("Incorrect password")
		return redirect ("/login")
# query the appt table for times that are today. 
#look at ratigs 
	day="01"
	year="2016"
	month="August"
	return render_template("appt_book.html", day=day, year=year, month=month)

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

@app.route ('/appt_book/<year>/<month>/<day>', methods=['GET'])
def show_appt_book(year,month,day,first_name):
	"""This will take the pts name and show the appt book"""
	first_name= request.args.post('first_name')

	return render_template ("appt_book.html", year=year, month=month, day=day, first_name=first_name)


@app.route ('/appt_book/<year>/<month>/<day>', methods=['POST'])
def appt_book_view(year,month,day):
	"""Appointment book view"""
	time_now= datetime.now()
	td= timedelta(1)
	first_available_day = time_now + td 
	weekdays= [Monday, Tuesday, Wednesday, Thursday,]
	if day in weekdays:
		first_available_day= time_now +td
	else: 
		first_available_day= time_now +timedelta(3)
		#get a code review for the above!!
	
	day="01"
	year="2016"
	month="August"
	#need the date, need to show all appts, need tp pass the day to the template. 
	appointments = {}
	# 	8: {
	# 		# user_id:
	# 		'first_name': 'Ruba',
	# 		'last_name': 'Hassan',
	# 		'appt_type': 'surgery',
	# 		'cost': 2000
	# 	},
	# 	14: {
	# 		# user_id:
	# 		'first_name': 'Kevin',
	# 		'last_name': 'Gao',
	# 		'appt_type': 'consultation',
	# 		'cost': 500
	# 	}
	# }
	# date = datetime.date(year, month, date)
	# today = datetime.now()
	# if today is dayof
 #need to pass in the day,month, year that come after the user logs in. This will only allow the user to make an appt for a day after they make the acct NOT same day. 
	return render_template("appt_book.html", year=year, month=month, day=day, appointments=appointments)

@app.route ('/confirm_appt', methods=['POST'])
def conf_appt():
	""" Need to send user to another page after appt has been confirmed"""

	appt_time = request.form.get('appt_time')
	first_name = session['first_name']
	
	return render_template("confirmation_page.html", first_name=first_name, appt_time=appt_time)
if __name__ == "__main__":
	
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host='0.0.0.0')





