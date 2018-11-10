from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from oddjobsapp.models import User, Post

class Index(generic.ListView):

    template_name = 'home/index.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')

def post(request):
    return HttpResponse("This is a dummy view")
