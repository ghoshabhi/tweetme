"""
tweetAPP URL Configuration
"""
from django.conf.urls import url
from .views import TweetListView, TweetDetailView
# tweet_list_view, tweet_detail_view,

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    # url(r'^$', tweet_list_view, name='list'),
    # url(r'^1/$', tweet_detail_view, name='detail'),
    url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^1/$', TweetDetailView.as_view(), name='detail'),
]
