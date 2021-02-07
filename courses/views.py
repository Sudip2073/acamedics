from django.shortcuts import render
from .models import Modules
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
@login_required(login_url='login')
def courses(request):
    return render(request,'courses.html')


def modules(request, mod_year):
    mod = Modules.objects.filter(year=mod_year)
    
    return render(request,'modules.html',
    {'mod': mod})


def modules_detail(request, Mod_code):
    try:
        Mod = Modules.objects.get(mod_code=str(Mod_code))
    except Modules.DoesNotExist:
        raise Http404('Modules not found')
    return render(request, 'sub_detail.html',{
        'Mod': Mod,
    })
