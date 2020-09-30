from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sample(request):
	return render(request,'dm1/home.html')

def prtname(t,n):
	return render(t,'dm1/name.html',{'name':n})

def twprt(request,rll,nm):
	return render(request,'dm1/rcd.html',{'name':nm,'roll':rll})

def rcrd(request,ag,nam,rll):
	return HttpResponse("<h2>Your Roll Number is: <span style='color:green'>{}</span> Your name is: <span style='color:red'>{}</span> Your age is: <span style='color:blue'>{}</span></h2>".format(rll,nam,ag))

def alt(request,nme,age):
	return HttpResponse("<script>alert('Hi Welcome {}')</script><h2>Your age is: {}</h2>".format(nme,age))

def dpform(request):
	return render(request,'dm1/inte.html')

def etfile(request):
	return render(request,'dm1/exter.html')