from database_functions import create_new_pt, create_new_appt, create_appt_type, create_new_owner

from model import connect_to_db, db,Appointment, Patient, AppointmentType, BusinessOwner

from server import app

from datetime import datetime

connect_to_db(app)

db.drop_all()

db.create_all()


def load_pts():
	"""Load patients from patients into database"""
	print "Patient"

	with open('./seed_data/patients.tsv','r+') as data:
		for i, row in enumerate(data):
			row = row.rstrip()
			first_name, last_name,date_of_birth, cell_phone_number, user_name, password = row.split ("\t")

			patient = Patient(
				first_name=first_name,
				last_name=last_name,
				date_of_birth=date_of_birth,
				cell_phone_number=cell_phone_number,
				user_name=user_name,
				password=password)

			db.session.add(patient)
			db.session.commit()

def create_appointment():
	"""To create the appointment"""
	with open('./seed_data/appt_type.tsv','r+') as data:
		for i, row in enumerate(data):
			row = row.rstrip()
			appt_type,appt_cost = row.split ("\t")
			appt_type = AppointmentType(
				appt_type=appt_type,
				cost=appt_cost)
			db.session.add(appt_type)
			db.session.commit()
	
	#d = datetime.strptime(appt_time, "%B %d, %Y")
	#example :appt_time= "August 18, 2016"
	
def create_provider():
	"""adding the provider in"""
	with open('./seed_data/drs.tsv','r+') as data:
		for i, row in enumerate(data):
			row = row.rstrip()
			print row.split(",")
			last_name, first_name,license_number,office_address,office_phone_number= row.split(",")
			
			provider=BusinessOwner(
				last_name=last_name,
				first_name=first_name,
				license_number=license_number,
				office_address=office_address,
				office_phone_number=office_phone_number)
			db.session.add(provider)
			db.session.commit()



if __name__ == '__main__':
	load_pts()

	create_appointment()

	create_provider()

# create_new_pt('ruba', 'hansan', '10101977', 6503012211, 'rubmnbhassan', '123456')
# ruba = Patient.query.filter_by(first_name='ruba').first()

# create_appt_type('Surgery', 1000)
# surgery = AppointmentType.query.filter_by(appt_type='Surgery').first()

# create_appt_type('Consultation', 500)
# cons = AppointmentType.query.filter_by(appt_type='Consultation').first()

# create_new_owner('Mike', 'Lee','123456','123 oak st','415772176')
# owner = BusinessOwner.query.filter_by(first_name='Mike').first()

# create_new_appt(ruba.user_id,cons.appt_type_id,'1pm Aug/16/2016',owner.provider_id)







