from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class ImgPfle(models.Model):
	use = models.OneToOneField(User,on_delete=models.CASCADE)
	im =  models.ImageField(upload_to="Profilepics/",null=True,default="demo.png")
	age = models.IntegerField(default=0)

@receiver(post_save,sender=User)
def Crtpfle(sender,instance,created,**kwargs):
	if created:
		ImgPfle.objects.create(use=instance)