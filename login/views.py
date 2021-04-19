from django.shortcuts import render,redirect
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    return render(request,'register.html')

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('dash')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dash')
            else:
                messages.info(request, 'SID or Password incorrect!')
                
        context={}
        #return render(request,'routines.html')
        return render(request,'login.html',context)

@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('login')

