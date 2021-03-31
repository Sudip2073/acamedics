from django.db import models

# Create your models here.
class Help(models.Model):
    reason= models.CharField(max_length=10)
    request= models.CharField(max_length=20)
    p= [        ('High','High'),
                ('Medium','Medium'),
                ('low','low')]
    priority= models.CharField(max_length=6,choices=p)

    def __str__(self):
        return str(self.reason)