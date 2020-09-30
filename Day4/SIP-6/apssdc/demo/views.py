from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sample(request):
	return HttpResponse("Hi Welcome to HomePage")