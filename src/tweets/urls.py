"""
tweetAPP URL Configuration
"""
from django.conf.urls import url
from .views import (
    TweetListView,
    TweetDetailView,
    TweetCreateView,
    TweetUpdateView,
    TweetDeleteView
    )
# tweet_list_view, tweet_detail_view, tweet_create_view


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    # url(r'^$', tweet_list_view, name='list'),
    # url(r'^1/$', tweet_detail_view, name='detail'),
    # url(r'^create/$', tweet_create_view, name='create'),
    url(r'^create/$', TweetCreateView.as_view(), name='create'),      # /tweet/create
    url(r'^$', TweetListView.as_view(), name='list'),                 # /tweet/
    url(r'^(?P<id>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1
    url(r'^(?P<pk>\d+)/edit/$', TweetUpdateView.as_view(), name='update'), # /tweet/1/update
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), # /tweet/1/delete
]
