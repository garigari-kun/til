from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Tweet

# def tweet_list_view(request):
#     template_name = 'tweets/tweet_list.html'
#     queryset = Tweet.objects.all()
#     context = {
#         'object_list': queryset
#     }
#     return render(request, template_name, context)
#

def tweet_detail_view(request, pk=None):
    template_name = 'tweets/tweet_detail.html'
    # obj = Tweet.objects.get(id=id)
    obj = get_object_or_404(Tweet, pk=pk)
    context = {
        'object': obj,
    }
    return render(request, template_name, context)


class TweetListView(ListView):
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = 'tweets/tweet_detail.html'
    #
    # def get_object(self):
    #     return Tweet.objects.get(id=1)
