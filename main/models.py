from django.db import models
from django.urls import reverse
# Create your models here.

class Temperature(models.Model):
    sensor_location = models.CharField("Місцезнаходження датчика", max_length=150)
    date = models.DateField("Дата заміру")
    time = models.TimeField("Час заміру")
    temperature = models.SmallIntegerField("Температура")
    sensor_name = models.CharField("Назва датчика", max_length=150)
    sensor_model = models.CharField("Модель датчика", max_length=150)
    url = models.SlugField(max_length=160, unique=True, null=False)


    def get_absolute_url(self):
        return reverse("temperature_detail", kwargs={"slug": self.url})

    def __str__(self):
        return self.sensor_name


class PdfMaker(models.Model):
    name = models.CharField("Назва", max_length=150)
    time = models.TimeField("Час публікації")
    type = models.CharField("Тип оповіщення", max_length=150)
    email = models.EmailField("Ел. почта")
    url = models.SlugField(max_length=160, unique=True, null=False)

    def get_absolute_url(self):
        return reverse("pdf_detail", kwargs={"slug": self.url})

    def __str__(self):
        return self.name