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
