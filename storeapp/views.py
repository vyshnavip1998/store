from django.shortcuts import render , redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,"home.html")
