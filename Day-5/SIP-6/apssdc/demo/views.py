from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sample(request):
	return HttpResponse("Hi Welcome to HomePage")

def prtname(t,n):
	return HttpResponse("Hi Welcome "+n)

def twprt(request,rll,nm):
	return HttpResponse("Hi Welcome {} and your roll number is: {}".format(nm,rll))

def rcrd(request,ag,nam,rll):
	return HttpResponse("<h2>Your Roll Number is: <span style='color:green'>{}</span> Your name is: <span style='color:red'>{}</span> Your age is: <span style='color:blue'>{}</span></h2>".format(rll,nam,ag))

def alt(request,nme,age):
	return HttpResponse("<script>alert('Hi Welcome {}')</script><h2>Your age is: {}</h2>".format(nme,age))
