"""Models and database functions for my app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
	"""Patient registration info"""

	__tablename__ = "patient"


	user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	first_name = db.Column(db.String(64), nullable=False)
	last_name = db.Column(db.String(64), nullable=False)
	date_of_birth = db.Column(db.String, nullable=False) 
	cell_phone_number = db.Column(db.String(64), nullable=False)
	user_name = db.Column(db.String(64), nullable=False)
	password = db.Column(db.String(64), nullable=False)

class BusinessOwner(db.Model):
	"""Business owner info"""

	__tablename__ = "Business_owner"

	provider_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	first_name = db.Column(db.String(64), nullable=False)
	last_name = db.Column(db.String(64), nullable=False)
	license_number = db.Column(db.String(64), nullable=False)
	office_address = db.Column(db.String(500), nullable=False)
	office_phone_number = db.Column(db.String(20), nullable=False)

class Appointment(db.Model):
	"""All Appointment info for my table"""

	__tablename__ = "appointment"

	appt_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('patient.user_id'), nullable=False)
	appt_time = db.Column(db.String, nullable=False)
	#appt_date = db.Column(db.Integer, nullable=False)
	appt_type_id = db.Column(db.Integer, db.ForeignKey('appointment_type.appt_type_id'), nullable=False)
	provider_id = db.Column(db.Integer,db.ForeignKey('Business_owner.provider_id'),nullable=False )

class AppointmentType(db.Model):
	"""Two different appointment types"""

	__tablename__ = "appointment_type"

	appt_type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	appt_type = db.Column(db.String, nullable=False)
	cost = db.Column(db.Integer, nullable=False)


def connect_to_db(app):
	"""Connect the database to our Flask app."""

	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///project'
	
	db.app = app
	db.init_app(app)

if __name__ == "__main__":
    
    from server import app
    connect_to_db(app)
    print "Connected to DB."