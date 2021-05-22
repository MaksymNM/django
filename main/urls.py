from django.urls import path
from . import views

urlpatterns = [
    path("", views.TemperatureView.as_view(), name='temperature_list'),
    path("<slug:slug>", views.TemperatureDetailView.as_view(), name='temperature_detail'),
    path("create/", views.TemperatureCreateView.as_view(), name='temperature_create'),
    path("export/<int:pk>", views.export, name='temperature_download'),
    path("pdf_list/", views.PdfMakerView.as_view(), name='pdf_list'),
    path("pdf_list/<slug:slug>/", views.PdfMakerDetail.as_view(), name='pdf_detail'),
    path("pdf_create/", views.PdfMakerCreateView.as_view(), name='pdf_create'),
    path("pdf_list/pdf_export/<int:pk>/", views.pdf_export, name='pdf_export'),
]