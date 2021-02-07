from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):
    user = models.OneToOneField (User, null= True, blank= True, on_delete=models.CASCADE)
    name= models.CharField(max_length=100)
    sid =  models.IntegerField(validators=[MinValueValidator(180000), MaxValueValidator(1901000)])
    sub_choice=[('E','BSc. (Hons) Ethical Hacking And Cybersecurity'),('CS','BSc. (Hons) Computing')]
    enrollement= models.CharField(max_length=100, choices = sub_choice)    
    age = models.IntegerField(null=True)
    email = models.EmailField()
    description = models.TextField(blank=True)
    year= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    profile_pic = models.ImageField(null=True, blank= True)

    def __str__(self):
        return str(self.user)
    


    
    
