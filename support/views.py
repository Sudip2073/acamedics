from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Help
from .forms import Supportform
# Create your views here.
@login_required(login_url='login')

def support(request):
    form= Supportform()
    if request.method == 'POST':
            form = Supportform(request.POST)
            if form.is_valid():
                form.save()
                
    context = {'form':form}
    return render(request,'Support.html',context)
