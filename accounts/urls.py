from django.conf.urls import url

from django.views.generic.base import RedirectView

from .views import (
	UserDetailView,
	UserFollowView
    )

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url="/")), 
    # url(r'^$', TweetListAPIView.as_view(), name='list'), # /api/tweet/
    # url(r'^create/$', TweetCreateAPIView.as_view(), name='create'), # /tweet/create/
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'), # /tweet/1/
    url(r'^(?P<username>[\w.@+-]+)/follow$', UserFollowView.as_view(), name='follow'), # /tweet/1/
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), # /tweet/1/update/
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), # /tweet/1/delete/
]
