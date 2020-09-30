from django.shortcuts import render,redirect
from enggapp.models import Register
from django.http import HttpResponse
from enggapp.forms import Usform

# Create your views here.
def register(request):
	if request.method=="POST":
		c=request.POST['cname']
		n=request.POST['name']
		r=request.POST['roll']
		b=request.POST['branch']
		y=request.POST['year']
		Register.objects.create(collegename=c,name=n,roll=r,branch=b,year=int(y))
		return redirect('/display')

	return render(request,'mytemplates/register.html')
def display(request):
	data=Register.objects.all()
	return render(request,'mytemplates/display.html',{'info':data})
def delete(request,id):
	data=Register.objects.get(id=id)
	data.delete()
	return redirect('/display')
def update(request,name):
	data=Register.objects.get(name=name)
	if request.method=="POST":
		c=request.POST['cname']
		n=request.POST['name']
		r=request.POST['roll']
		b=request.POST['branch']
		y=request.POST['year']
		data.collegename=c
		data.name=n
		data.roll=r
		data.branch=b
		data.year=y
		data.save()
		return redirect('/display')
	return render(request,'mytemplates/update.html',{'info':data})


def userreg(request):
	if request.method == "POST":
		l=Usform(request.POST)
		if l.is_valid():
			l.save()
			return render(request, sh)
	p = Usform()
	return render(request,'mytemplates/userrg.html',{'usg':p})

def show(request):
	r = Register.objects.all()
	return render(request,"mytemplates/show.html",{'s':r})
def dlt(request,id):
	d = Register.objects.get(id=id)
	d.delete()
	return HttpResponse("User deleted successfully....")





