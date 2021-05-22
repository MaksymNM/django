from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseNotFound
from reportlab.pdfgen import canvas

from .models import *
import json

import io
from django.http import FileResponse



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

def export(request, pk):
    bd = Temperature.objects.get(id=pk)
    data = {'name': str(bd.sensor_location), 'date': str(bd.date), 'time': str(bd.time), 'temperature': str(bd.temperature), 'sensor_name': str(bd.sensor_name), 'sensor_model': str(bd.sensor_model), 'url': str(bd.url)}
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="members.json"'
    return response


class PdfMakerView(ListView):
    model = PdfMaker
    queryset = PdfMaker.objects.all()


class PdfMakerDetail(DetailView):
    model = PdfMaker
    slug_field = "url"

class PdfMakerCreateView(CreateView):
    model = PdfMaker
    fields = ('name', 'time', 'type', 'email', 'url')

def pdf_export(request, pk):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    bd = PdfMaker.objects.get(id=pk)
    p.drawString(100, 50, bd.name)
    p.drawString(100, 100, str(bd.time))
    p.drawString(100, 150, bd.type)
    p.drawString(100, 200, bd.email)
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='download.pdf')

    '''Отображение только для авторизованных пользователей'''
def index(request):
    context = {
        'temperature_list': Temperature.objects.all()
        if request.user.is_authenticated else []
    }
    return render(request, 'pressure\secure.html', context)
