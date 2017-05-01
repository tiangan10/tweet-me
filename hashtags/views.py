from django.shortcuts import render
from django.views import View

# Create your views here.

from .models import HashTag

class HashTagView(View):
	def get(self, request, hashTag, *args, **kwargs):
		obj, created = HashTag.objects.get_or_create(tag=hashTag)
		return render(request, 'hashtags/tag_view.html', {"obj" : obj})