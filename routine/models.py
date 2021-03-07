from django.db import models

# Create your models here.

class routiney(models.Model):
    batch= models.CharField(max_length=5)
    img=models.ImageField()