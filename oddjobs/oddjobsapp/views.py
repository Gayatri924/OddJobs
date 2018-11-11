from django.http import HttpResponse
from django.views import generic
from oddjobsapp.models import User, Post
from oddjobsapp.forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from stream_django.feed_manager import feed_manager
from django.views.generic.edit import CreateView
from oddjobsapp.models import Post

class PostView(CreateView):
    model = Tweet
    fields = ['text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Tweet, self).form_valid(form)

class Index(LoginRequiredMixin, generic.ListView):
  login_url = '/login'
  redirect_field_name = ''

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
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

class Index(generic.ListView):

    template_name = 'home/index.html'
    context_object_name = 'posts_list'

    def get_queryset(user_id):
        return feed_manager.get_user_feed(user_id)

def post(request):
    return HttpResponse("This is a dummy view")
