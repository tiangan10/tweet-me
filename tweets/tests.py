from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
from .models import Tweet

User = get_user_model()

class TweetModelTestCase(TestCase):
	def setUp(self):
		print("called")
		a_user = User.objects.create(username="jimmy")

	def test_tweet_item(self):
		obj = Tweet.objects.create(
				user = User.objects.first(),
				content = 'some random tweet'
			)
		self.assertTrue(obj.content == 'some random tweet')
		self.assertTrue(obj.id == 1)

	def test_tweet_url(self):
		obj = Tweet.objects.create(
				user = User.objects.first(),
				content = 'some random tweet'
			)
		absolute_url = reverse("tweet:detail", kwargs={"pk" : obj.pk})
		self.assertEqual(obj.get_absolute_url(), absolute_url)

