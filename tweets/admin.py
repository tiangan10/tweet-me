from django.contrib import admin

# Register your models here.
from .models import Tweet
from .forms import TweetModelForm

class TweetModelAdmin(admin.ModelAdmin):
	class Meta:
		model = Tweet
	#form = TweetModelForm

admin.site.register(Tweet, TweetModelAdmin)
