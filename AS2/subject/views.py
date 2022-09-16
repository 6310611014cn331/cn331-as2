from django.shortcuts import render
from .models import detail, quotas
# Create your views here.

def index(request):
    subject = detail.objects.all()
    return render(request, "subject\\index.html", {"subject":subject
    })

def subject(request, subject_id):
    s = detail.objects.get(pk=subject_id)
    return render(request, 'subject\\subjects.html',{'subject' : s})
