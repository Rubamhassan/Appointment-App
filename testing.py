
import unittest
from server import app
from model import db, example_patient, example_business_owner, connect_to_db, example_patient

class PatientTest(unittest.TestCase):
	"""Test for patient"""

	def setUp(self):
		self.client = app.test_client()
		app.config['TESTING'] = True

	def test_homepage(self):
		result = self.client.get("/")
		self.assertIn("Bay Area Oral & Maxillofacial Surgery", result.data)

	def test_plogin_page(self):
		result = self.client.get("/plogin")
		self.assertIn("New Patient Registration Form", result.data)

	def test_owner_login_page(self):
		result = self.client.get("/owner_login")
		self.assertIn("Provider Login", result.data)

	def test_owner_login_page(self):
		result = self.client.get("/login")
		self.assertIn("Please choose one of the following options", result.data)



class PatientTestDatabase(unittest.TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()


if __name__ == "__main__":
    unittest.main()


