"""APSSDC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from enggapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register,name="rg"),
    path('display/',views.display,name='dis'),
    path('delete/<int:id>/',views.delete,name='del'),
    path('update/<str:name>/',views.update,name='up'),
    path('usrg/', views.userreg, name="usg"),
    path('shw/',views.show,name="sh"),
    path('dlu/<int:id>/',views.dlt,name="det")

]
