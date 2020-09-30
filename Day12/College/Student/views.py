from django.shortcuts import render

# Create your views here.
def insert(request):
	return render(request,'mytemplates/insert.html')