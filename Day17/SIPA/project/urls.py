from django.urls import path
from project import views
from django.contrib.auth import views as t


urlpatterns = [
		path("",views.home,name="hme"),
		path('about/',views.about,name="abt"),
		path('reg/',views.usrg,name="ug"),
		path('login/', t.LoginView.as_view(template_name="demo/login.html"), name='lg'),
		path('dashbord/',views.db,name="db"),
		path('logout/',t.LogoutView.as_view(template_name='demo/logout.html'),name='lo'),
		path('profile/',views.profile,name='pf'),

]
