from django.db import models

# Create your models here.
# from django.db import models
from django.db.models import Model
# Create your models here.
# python manage.py makemigrations-> create changes and store in file
# migrate->apply the pending changes created by the makemigrations

# class GeeksModel(Model):
# 	geeks_field = models.CharField(
# 					max_length = 200,
# 					verbose_name = "Geeksforgeeks"
# 					),
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()
    
	# def __str__(self):
	# 	return self.name