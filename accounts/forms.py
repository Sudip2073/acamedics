from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class Accountform(ModelForm):
	class Meta:
		model = Student
		fields = '__all__'
		exclude = ['user','sid']