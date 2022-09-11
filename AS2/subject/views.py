from django.shortcuts import render
from .models import detail
# Create your views here.

def index(request):
    e_subject = detail.objects.all()
    return render(request, 'subject/index.html')
    {
        'subject' : subject
    }