# Generated by Django 3.1.7 on 2021-05-22 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210522_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='PdfMaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Назва')),
                ('time', models.TimeField(verbose_name='Час публікації')),
                ('type', models.CharField(max_length=150, verbose_name='Тип оповіщення')),
                ('email', models.EmailField(max_length=254, verbose_name='Ел. почта')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
        ),
    ]
