from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required

# Create your views here.

def support(request):
    #return render(request,'routines.html')
    return render(request,'support.html')
