## Synopsis
  
Appointment Scheduler is an app that allows new and existing patients to log in and schedule an appointment with their doctor based on what times and dates are available. Which can maximize the office production by giving the patient the opportunity to schedule when they are ready and need the appointment. With the calendar set up with datetime, It will show real time dates and only allow the user to schedule two business days in advance from when they sign in.  My calendar has the benifit of having two views, one for the doctor and one for the patient.The doctor also has the benefit to see what and who is scheduled anytime and can access the app remotely. 

![homepage](/static/homepage.jpeg?raw=true "Homepage")

Patient Log in:
![Patient login](/static/patientlogin.jpeg?raw=true "Patient Log in page")

Once user is logged in:
![User page](/static/onceuserloggedin.jpeg?raw=true "Once user is logged in")

Schedule view for patient: 
![Schedule view for patient](/static/patientscheduleview.jpeg?raw=true"Schedule view for patient")

Confirmed page:
![Confirmed page](/static/confirmedpage.jpeg?raw=true "Confirmed page")

Provider Log in page:
![Provider log in page](/static/providerloginpage.jpeg?raw=true "Provider Log in page")

Schedule view for the doctor:
![schedule view for the doctor](/static/drsviewofschedule.jpeg?raw=true "Schedule view for the doctor")


## Installation
Appointment App requires a requirements.txt file installation. Appointment App runs through the server.py file on http://localhost:5000/


## API Reference

Appointment App is using a Twilio api for text messaging to confirm the scheduled appointments.

## Tests

Tests for Appointment App are located in testing.py . Appointment App offers 56% test coverage through unittests. Testing covers assertions on all pages on Appointment App, and ensures that when a user moves from one html to another it displays the correct page.

## Tech Stack
Python, Javascript, JQuery, Jinja, SQL, SQLAlchemy, , HTML, CSS, Coverage 


