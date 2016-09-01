from model import connect_to_db,db, Patient, BusinessOwner, Appointment, AppointmentType
from datetime import datetime, timedelta

def create_new_pt(first_name,
				  last_name,
				  date_of_birth,
				  cell_phone_number,
				  user_name,
				  password):


	"""This function is to create a new patient"""
	patient = Patient(first_name=first_name, 
					  last_name=last_name, 
					  date_of_birth=date_of_birth, 
					  cell_phone_number=cell_phone_number, 
					  user_name=user_name,
					  password=password)
	db.session.add(patient)
	db.session.commit()

	return patient

def create_new_appt(user_id,appt_type_id,appt_time,provider_id,appt_date):
	"""This function is to create a new appointment"""
	new_appt = Appointment(user_id=user_id, appt_type_id=appt_type_id,appt_time=appt_time, provider_id= provider_id, appt_date=appt_date)
	db.session.add(new_appt)
	db.session.commit()
	return new_appt

def create_appt_type(appt_type,cost):
	"""two types of appointments"""
	appt_type = AppointmentType(appt_type= appt_type, cost= cost)
	db.session.add(appt_type)
	db.session.commit()
	return appt_type


def create_new_owner(first_name,last_name,license_number,office_address,office_phone_number):
	"""This is to create a new owner"""
	new_owner = BusinessOwner(first_name=first_name,
							last_name=last_name,
							license_number=license_number,
							office_address=office_address,
							office_phone_number=office_phone_number)
	db.session.add(new_owner)
	db.session.commit()
	return new_owner

def next_aval_date():
	"""returns the first available date for user

		>>> type(next_aval_date())
		<type 'tuple'>

	"""
	time_now= datetime.now()
	td= timedelta(1)

	first_available_day = time_now + td 
	weekdays= ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
	for day in weekdays:
		if day in weekdays:
			first_available_day= time_now +td
		else: 
			first_available_day= time_now +timedelta(3)
	return (first_available_day.day, first_available_day.month, first_available_day.year)






