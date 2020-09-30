from django.db import models

# Create your models here.
class Register(models.Model):
	collegename=models.CharField(max_length=50)
	name=models.CharField(max_length=50)
	roll=models.CharField(max_length=20)
	branch=models.CharField(max_length=50)
	year=models.IntegerField()
