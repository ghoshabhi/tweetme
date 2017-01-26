'''
Views for Tweets app
'''
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Tweet
# Create your views here.

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    def get_object(self):
        print self.kwargs
        id = self.kwargs.get('id')
        return Tweet.objects.get(id=id)

class TweetListView(ListView):
    queryset = Tweet.objects.all()

    # custom method to give a context
    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        # context["abhi"] = "Ghosh"
        # print context
        return context

# def tweet_detail_view(request, id=1):
#     '''
#     Detail View for tweet
#     '''
#     obj = Tweet.objects.get(id=id)
#     # print obj
#     context = {
#         "object": obj
#     }
#     return render(request, "tweets/detail_view.html", context)
#
# def tweet_list_view(request, id=1):
#     '''
#     Detail List for tweet
#     '''
#     queryset = Tweet.objects.all()
#     # print queryset
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "tweets/list_view.html", context)
