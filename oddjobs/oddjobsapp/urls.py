from django.urls import path, include
from django.views.generic import TemplateView, DetailView
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from oddjobsapp import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('post/', views.PostView.as_view(template_name="posts/post.html"), name='post'),
    #path('login/', views. , name='login'),
    path('general.css', TemplateView.as_view(template_name="home/general.css"), name = "general"),
#<<<<<<< HEAD
    path('secret.txt', TemplateView.as_view(template_name="home/secret.txt"), name = "secret"),
    #path('Logo.png', TemplateView.as_view(template_name="posts/Logo.png"), name = "logo"),
#=======
#    path('oddjobs.css', TemplateView.as_view(template_name="templates/registration/oddjobs.css"), name = "oddjobs"),
#>>>>>>> master
    #path('bkgd.png', TemplateView.as_view(template_name="home/bkgd.png"), name = "background"),
    path('index.js', TemplateView.as_view(template_name="home/index.js"), name = "index_js"),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
#<<<<<<< HEAD
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('feed/', views.FeedView.as_view(), name='feed'),
    path('posts/', views.PostsView.as_view(), name="posts"),
#=======
#    path('logout/', auth_views.logout, name='logout'),
#    path('admin/', admin.site.urls),
#    path('timeline/', login_required(views.PostView.as_view()), name='timeline'),
#>>>>>>> master
]
