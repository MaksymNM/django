from django.urls import path
from . import views

urlpatterns = [
    path("", views.TemperatureView.as_view(), name='temperature_list'),
    path("<slug:slug>", views.TemperatureDetailView.as_view(), name='temperature_detail'),
    path("create/", views.TemperatureCreateView.as_view(), name='temperature_create'),

]