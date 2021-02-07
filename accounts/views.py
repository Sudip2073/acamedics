from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .forms import Accountform

# Create your views here.

@login_required(login_url='login')
def account(request):
    user = request.user.student
    form = Accountform(instance=user)

    if request.method == 'POST':
        form= Accountform(request.POST, request.FILES, instance= user)
        if form.is_valid():
            form.save()


    context= {'form': form}
    return render(request,'account_setting.html',context)