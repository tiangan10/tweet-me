from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import UserProfile

# Create your tests here.

User = get_user_model()

class UserProfileTestCase(TestCase):
	def setUp(self):
		self.username = "someUser"
		new_user = User.objects.create(username = self.username)

	def test_profile_created(self):
		username = self.username
		user_profile = UserProfile.objects.filter(user__username = self.username)
		self.assertTrue(user_profile.exists())
		self.assertTrue(user_profile.count() == 1)

	def test_new_user(self):
		try:
			User.objects.create(username = self.username)
			self.fail("Should not allow create with existing username")
		except:
			print("existed")
			pass