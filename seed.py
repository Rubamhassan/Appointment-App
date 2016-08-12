from database_functions import create_new_pt, create_new_appt, create_appt_type, create_new_owner

from model import connect_to_db, db,Appointment, Patient, AppointmentType, BusinessOwner

from server import app

connect_to_db(app)

db.drop_all()

db.create_all()

# this is example code to add many users from seed file
# f = open('seed_data/user')

# for line in f:
# 	row = line.rstring().split('|')
# 	first_name = row[0]
# 	last_name = row[1]


create_new_pt('ruba', 'hansan', '10101977', 6503012211, 'rubmnbhassan', '123456')
ruba = Patient.query.filter_by(first_name='ruba').first()

create_appt_type('Surgery', 1000)
surgery = AppointmentType.query.filter_by(appt_type='Surgery').first()

create_appt_type('Consultation', 500)
cons = AppointmentType.query.filter_by(appt_type='Consultation').first()

create_new_owner('Mike', 'Lee','123456','123 oak st','415772176')
owner = BusinessOwner.query.filter_by(first_name='Mike').first()

create_new_appt(ruba.user_id,cons.appt_type_id,'1pm Aug/16/2016',owner.provider_id)







