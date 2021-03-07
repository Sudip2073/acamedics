from django.shortcuts import render
from .models import Notify
# Create your views here.
def notify(request):
    notice = Notify.objects.all()

    return render (request,'notification.html',{
        'notice' : notice
    })

