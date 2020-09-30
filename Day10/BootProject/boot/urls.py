from django.urls import path
from boot import views

urlpatterns = [
	path("",views.home,name="hme"),
	path("abt/",views.about,name="ab"),
]
