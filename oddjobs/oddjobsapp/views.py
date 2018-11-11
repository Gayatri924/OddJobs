from django.http import HttpResponse
from django.views import generic
from oddjobsapp.models import User, Post
#<<<<<<< HEAD
from oddjobsapp.forms import SignUpForm
#=======
#from oddjobsapp.forms import SignUpForm, PostForm
#>>>>>>> master
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
#<<<<<<< HEAD
from oddjobsapp.models import Post
from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager
from django.contrib.auth.models import User
from django.views.generic import DetailView
import stream

class PostView(CreateView):
    model = Post
    fields = ['text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Post,self).form_valid(form)

class Index(LoginRequiredMixin, generic.ListView):
  login_url = '/login'
  redirect_field_name = ''

def addPost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                created_at = form.cleaned_data.get('created_at')
                user = form.cleaned_data.get('user')
                text = form.cleaned_data.get('text')
                client = stream.connect('7a7vvthtmw7d', 'dxm9bj3zdgvf84jq4m9h362svdmz8neqfryptc9jsfkhur5nz5tbvmhyt9arbrqd')
                feed = client.feed('user', user)
                feed.add_activity({'actor': user, 'verb': 'Post', 'object': 1, 'tweet': text})

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/feed')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


class PostsView(generic.ListView):

    template_name = 'posts/posts.html'
    context_object_name = 'posts_list'

    def get_queryset(user_id):
        return HttpResponse("Hi");

#<<<<<<< HEAD
class Index(generic.ListView):

    template_name = 'home/index.html'
    context_object_name = 'posts_list'

    def get_queryset(user_id):
        return HttpResponse("Hi");
        #return feed_manager.get_user_feed(user_id)

def post(request):
    return HttpResponse("This is a dummy view")

enricher = Enrich()

class FeedView(DetailView):
    model = User
    template_name = 'posts/feed.html'
    def get_object(self):
        return self.get_queryset().get(username="shell")

    def get_context_data(self, object):
        user = self.object
        feed = feed_manager.get_feed('timeline','shell')
        activities = feed.get()['results']
        activities = enricher.enrich_activities(activities)
        return {
            'activities': activities,
            'user': user,
            'login_user': self.request.user
        }
