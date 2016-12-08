from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView


from .models import Tweet
from .forms import TweetModelForm


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


class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweets/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)


def tweet_create_view(request):
    form = TweetModelForm(request.POST or None)
    template_name = 'tweets/create_view.html'
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
    context = {
        'form': form,
    }

    return render(request, template_name, context)
