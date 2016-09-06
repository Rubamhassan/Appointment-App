## Synopsis
  
Appointment Scheduler is an app that allows new and existing patients to log in and schedule an appointment based on available times and dates. This can maximize the office production as it gives the patients the (freedom) opportunity to schedule their appointments when they are able to and at the time that is convenient for them. The calendar set-up with datetime shows real time dates and only allows the user to schedule two business days in advance. My calendar has the benefit of having two views: one for the patient and one for the doctor. The doctor has the added benefit of seeing who has scheduled an appointment at any time, both in the office and remotely.

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
![schedule view for the doctor](/static/doctorsview.jpeg?raw=true "Schedule view for the doctor")


## Installation
Appointment App requires a requirements.txt file installation. Appointment App runs through the server.py file on http://localhost:5000/


## API Reference

Appointment App is using a Twilio api for text messaging to confirm the scheduled appointments.

## Tests

Tests for Appointment App are located in testing.py . Appointment App offers 56% test coverage through unittests. Testing covers assertions on all pages on Appointment App, and ensures that when a user moves from one html to another it displays the correct page.

## Tech Stack
Python, Javascript, JQuery, Jinja, SQL, SQLAlchemy, , HTML, CSS, Coverage 


