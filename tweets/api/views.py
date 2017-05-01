from rest_framework import generics
from rest_framework import permissions
from django.db.models import Q

from tweets.models import Tweet
from .serializers import TweetModelSerializer
from .pagination import StandardResultsPagination

class TweetCreateAPIView(generics.CreateAPIView):
	serializer_class = TweetModelSerializer
	permission_classes = [permissions.IsAuthenticated]
	def perform_create(self, serializer):
		serializer.save(user = self.request.user)

class TweetListAPIView(generics.ListAPIView):
	serializer_class = TweetModelSerializer
	pagination_class = StandardResultsPagination

	def get_queryset(self, *args, **kwargs):
		print(type(self.request.user))
		im_following = self.request.user.profile.get_following()
		qs1 = Tweet.objects.filter(user__in=im_following)#.order_by('-timestamp')
		qs2 = Tweet.objects.filter(user=self.request.user)
		qs = (qs1 | qs2).distinct()
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
					Q(content__icontains=query) |
					Q(user__username__icontains=query)
				)
		return qs