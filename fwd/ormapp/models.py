from django.db import models
from django.contrib import admin
class swiggy(models.Model):
    fid=models.IntegerField()
    fname=models.CharField(max_length=100)
    collection=models.IntegerField()
    year=models.IntegerField()
    rating=models.FloatField()

class swiggyAdmin(admin.ModelAdmin):
    list_display=('fid','fname','collection','year','rating')
    