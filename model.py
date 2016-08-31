"""Models and database functions for my app"""

from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship

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

	appointments = db.relationship("Appointment")

# def example_patient():
# 	patient = Patient(user_id=9999, first_name="Mickey",
# 	last_name="Mouse", date_of_birth="01/05/2012",
# 	cell_phone_number="4152157711", user_name="MickeyMouse",
# 	password="123456") 

# 	db.session.add(example_patient)
#     db.session.commit()


class BusinessOwner(db.Model):
	"""Business owner info"""

	__tablename__ = "business_owner"
#need to make provider ID autoincremenet=True
	provider_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	first_name = db.Column(db.String(64), nullable=False)
	last_name = db.Column(db.String(64), nullable=False)
	license_number = db.Column(db.String(64), nullable=False)
	office_address = db.Column(db.String(500), nullable=False)
	office_phone_number = db.Column(db.String(20), nullable=False)

def example_business_owner():
	business_owner = BusinessOwner(provider_id = 9191, first_name = "Ron",
					last_name = "Jones", license_number ="12345",
					office_address = "121 Sutter St. SF", office_phone_number ="4152153322")


class Appointment(db.Model):
	"""All Appointment info for my table"""

	__tablename__ = "appointment"

	appt_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('patient.user_id'), nullable=False)
	appt_time = db.Column(db.String, nullable=False)
	appt_date = db.Column(db.String, nullable=False)
	appt_type_id = db.Column(db.Integer, db.ForeignKey('appointment_type.appt_type_id'), nullable=False)
	provider_id = db.Column(db.Integer,db.ForeignKey('business_owner.provider_id'),nullable=False )

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class AppointmentType(db.Model):
	"""Two different appointment types"""

	__tablename__ = "appointment_type"
 #do we need to make this autoincrement?
	appt_type_id = db.Column(db.Integer, primary_key=True)
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