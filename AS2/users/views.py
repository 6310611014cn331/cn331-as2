#from audioop import reverse
#from xml.dom import InvalidAccessErr
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return render(request, "users\\login.html", {"message":"Invalid credentials."})

def logout_view(request):
    pass
    #return render(request, "users/logout.html")