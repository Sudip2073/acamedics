from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required

# Create your views here.


def rou(request):
    #return render(request,'routines.html')
    return render(request,'routines.html')
    
