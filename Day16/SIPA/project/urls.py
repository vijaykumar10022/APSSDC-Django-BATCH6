from django.urls import path
from project import views

urlpatterns = [
		path("",views.home,name="hme"),
		path('about/',views.about,name="abt"),
		path('reg/',views.usrg,name="ug"),
]
