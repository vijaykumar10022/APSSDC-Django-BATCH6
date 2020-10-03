from django.urls import path
from project import views
from django.contrib.auth import views as t

urlpatterns = [
		path("",views.home,name="hme"),
		path('about/',views.about,name="abt"),
		path('reg/',views.usrg,name="ug"),
		path("login/",t.LoginView.as_view(template_name="demo/login.html"),name="lg"),
		path("logout/",t.LogoutView.as_view(template_name="demo/logout.html"),name="lgo"),
		path('dsh/',views.dash,name="dsb"),
		path('pfle/',views.prfle,name="pf"),
		path('updf/',views.updfle,name="upf"),
]
