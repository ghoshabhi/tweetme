'''
Views for Tweets app
'''
from django.shortcuts import render
from .models import Tweet
# Create your views here.

def tweet_detail_view(request, id=1):
    '''
    Detail View for tweet
    '''
    obj = Tweet.objects.get(id=id)
    # print obj
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", context)

def tweet_list_view(request, id=1):
    '''
    Detail List for tweet
    '''
    queryset = Tweet.objects.all()
    # print queryset
    context = {
        "object_list": queryset
    }
    return render(request, "tweets/list_view.html", context)
