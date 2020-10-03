from django.shortcuts import render,redirect
from project.forms import UsRgt,Usupfle,Impf
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from project.models import ImgPfle

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
			return redirect('/login')
	t = UsRgt()
	return render(request,'demo/registration.html',{'y':t})

@login_required
def dash(request):
	return render(request,'demo/dashboard.html')

@login_required
def prfle(request):
	return render(request,'demo/profile.html')

@login_required
def updfle(request):
	# y = User.objects.get(id=request.user.id)
	if request.method == "POST":
		q = Usupfle(request.POST,instance=request.user)
		r = Impf(request.POST,request.FILES,instance=request.user.imgpfle)
		if q.is_valid() and r.is_valid():
			q.save()
			r.save()
			return redirect('/pfle')
	q = Usupfle(instance=request.user)
	r = Impf(instance=request.user.imgpfle)
	return render(request,'demo/updateprofile.html',{'f':q,'t':r})