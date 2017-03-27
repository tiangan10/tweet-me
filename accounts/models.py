from django.conf import settings
from django.db import models

# Create your models here.
class UserProfileManager(models.Manager):

	def get_queryset(self):
		qs = super(UserProfileManager, self).get_queryset()
		if self.instance:
			qs = qs.exclude(user = self.instance)
			print("yes, excluded")
		return qs


class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
	following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')
	objects = UserProfileManager()

	def __str__(self) :
		return str(self.user.username)

	def get_following(self):
		users = self.following.all()
		print("here we are:")
		print(self.following)
		return users.exclude(username = self.user.username)