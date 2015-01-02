from django.db import models

# Create your models here.

class Biisi(models.Model):
    nimi = models.CharField(max_length=200)
    esittaja = models.CharField(max_length=200) 
    soinnut = models.CharField(max_length=200)
    linkki = models.CharField(max_length=200)
