from django.db import models

# Create your models here.

class ADDDATA(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Number=models.CharField(max_length=100,null=True,blank=True)
    Location=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.Name