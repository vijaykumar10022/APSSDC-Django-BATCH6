from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request,'boot1/home.html')

def about(request):
	return render(request,'boot1/about.html')