from django.shortcuts import render
from project.forms import UsRgt
from django.contrib import messages

# Create your views here.

def home(request):
	return render(request,'demo/home.html')

def about(request):
	return render(request,'demo/about.html')

def usrg(request):
	if request.method == "POST":
		t = UsRgt(request.POST)
		if t.is_valid():
			t.save()
			messages.success(request,"User Registered Successfully")
	t = UsRgt()
	return render(request,'demo/registration.html',{'y':t})