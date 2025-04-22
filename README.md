# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).


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
from .models import Movie,MovieAdmin
admin.site.register(Movie,MovieAdmin)

model.py

from django.db import models
from django.contrib import admin
class Movie(models.Model):
	Name=models.CharField(max_length=20,primary_key=True)
	Genre=models.CharField(max_length=20)
	Cost=models.CharField(max_length=20)
	Run=models.CharField(max_length=20)
	Rating=models.IntegerField()
class MovieAdmin(admin.ModelAdmin):
	list_display=("Name","Genre","Cost","Run","Rating")

```


## OUTPUT

![alt text](movie.png)



## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
