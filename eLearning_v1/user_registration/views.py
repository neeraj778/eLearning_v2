from django.shortcuts import render
from django.http import HttpResponse
from .models import users, courses

# Create your views here.

def index(request):
	context = {
			"courses" : courses.objects.all()
	};
	return render(request,"index.html",context);