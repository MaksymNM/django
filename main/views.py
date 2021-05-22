from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseNotFound
from .models import *



# Create your views here.

class TemperatureView(ListView):

    model = Temperature
    queryset = Temperature.objects.all()


class TemperatureDetailView(DetailView):
    model = Temperature
    slug_field = "url"

class TemperatureCreateView(CreateView):
    model = Temperature
    fields = ('sensor_location', 'date', 'time', 'temperature', 'sensor_name', 'sensor_model', 'url')

