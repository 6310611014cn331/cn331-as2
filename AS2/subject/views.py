from django.shortcuts import render
from .models import detail, quotas
from django.urls import reverse, exceptions
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    subject = detail.objects.all()
    try:
        return render(request, "subject/index.html", {"subject":subject
        })
    except exceptions.NoReverseMatch:
        return HttpResponseRedirect(reverse("login"))

def subject(request, subject_id):
    s = detail.objects.get(pk=subject_id)
    try:
        return render(request, 'subject/subjects.html',{'subject' : s})
    except exceptions.NoReverseMatch:
        return HttpResponseRedirect(reverse("login"))
