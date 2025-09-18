from django.db import models
from django.contrib import admin
class Car(models.Model):
    carnumber=models.IntegerField()
    mname=models.CharField(max_length=100)
    price=models.IntegerField()
    year=models.IntegerField()
    colour=models.CharField()

class CarAdmin(admin.ModelAdmin):
    list_display=('carnumber','mname','price','year','colour')
