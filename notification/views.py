from django.shortcuts import render
from .models import Notify
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def notify(request):
    notice = Notify.objects.all()

    return render (request,'notification.html',{
        'notice' : notice
    })


