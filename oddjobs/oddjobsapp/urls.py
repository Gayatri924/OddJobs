from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('post/', views.post, name='post'),
    #path('login/', views. , name='login'),
    path('general.css', TemplateView.as_view(template_name="home/general.css"), name = "general"),
    #path('bkgd.png', TemplateView.as_view(template_name="home/bkgd.png"), name = "background"),
    path('index.js', TemplateView.as_view(template_name="home/index.js"), name = "index_js"),
]
