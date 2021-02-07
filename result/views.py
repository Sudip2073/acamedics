from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def result(request):
    #return render(request,'routines.html')
    return render(request,'result.html')
