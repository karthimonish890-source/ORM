# Ex02 Django ORM Web Application
## Date: 25/11/2026
## Ref no:26012370

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import swiggy,swiggyAdmin
admin.site.register(swiggy,swiggyAdmin)

models.py 

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

```


## OUTPUT

![alt text](<Screenshot 2026-11-25 162219.png>)


## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
