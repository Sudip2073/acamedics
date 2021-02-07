from django.db import models
from django.core.validators import *


# Create your models here.
class Modules(models.Model):    #Subject i.e. Digital forensics
    name= models.CharField(max_length=100)
    category= [
                ('1','1'),
                ('2','2'),
                ('3','3')]
    year= models.CharField(max_length=100,choices= category)  #Available year
    mod_code= models.CharField(max_length=9,validators=[MinLengthValidator(5), MaxLengthValidator(9)])
    description= models.TextField()
    credit= models.IntegerField()

    