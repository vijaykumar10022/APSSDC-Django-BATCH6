from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jsf(request):
	return render(request,'myapp1/jsindex.html')
def bs(request):
	return render(request, 'myapp1/bsindex.html')
def ob(request):
	return render(request, 'myapp1/obindex.html')
def register(request):
	if request.method=="POST":
		return HttpResponse("Uplode Successully")
	return render(request, 'myapp1/register.html')