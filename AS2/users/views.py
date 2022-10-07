from operator import sub
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from users.models import user_quotas
from subject.models import quotas as op_quota
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/u_index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("u_index"))
        else:
            return render(request, "users/login.html", {"message":"Invalid credentials."})
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message":"You are logged out"})

def quotas(request, username):
    user = User.objects.get(username=username)
    u = (user.usequota.get()).id
    q = user_quotas.objects.get(pk=u)
    return render(request, "users/quotas.html", {
        "subselect":  q.subject.all(), 
        "nonselect":op_quota.objects.exclude(user_quota=q).all(),
        "day":op_quota.days,
        "time":op_quota.time,
    })

def subtract(value, arg):
    return value - arg

def book(request,  username):
    user = User.objects.get(username=username)
    u = (user.usequota.get()).id
    if request.method == "POST":
        subject = user_quotas.objects.get(pk=u)
        quotas = op_quota.objects.get(pk=request.POST["quotas"])
        subject.subject.add(quotas)
        quotas.sit = quotas.sit - subject.amount_taken
        quotas.save()
        return HttpResponseRedirect(reverse("quotas", args=(username,)))

def delete(request, username, s_id):
    user = User.objects.get(username=username)
    u = (user.usequota.get()).id
    subject = user_quotas.objects.get(pk=u)
    quotas = op_quota.objects.get(pk=s_id)
    quotas.delete()
    quotas.sit = quotas.sit + subject.amount_taken
    quotas.save()
    return HttpResponseRedirect(reverse("quotas", args=(username,)))
