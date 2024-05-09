from .models import Direction
from django.shortcuts import render
from django.views import generic


# Create your views here.

class HomePageView(generic.ListView):
    model = Direction
    template_name = 'documents/home.html'
    context_object_name = 'directions'


