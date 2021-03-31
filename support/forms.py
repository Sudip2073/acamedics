from django.forms import ModelForm
from django.contrib.auth.models import User

from django import forms


from .models import *

class Supportform(ModelForm):
	class Meta:
		model = Help
		fields = '__all__'
		