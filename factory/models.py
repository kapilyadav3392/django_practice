from django.db import models


# Create your models here.

class data(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20, default='')
    Birthdate=models.CharField(max_length=50,default='')
    image=models.ImageField(default='')
    
    def __str__(self):
        return self.name
    
class user(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField( max_length=50)
    name=models.CharField( max_length=20)
    password=models.CharField( max_length=8)
    
class detail(models.Model):
    id=models.AutoField(primary_key=True)
    dataid=models.ForeignKey(data,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    image=models.ImageField(default='')
    age=models.IntegerField(default='18')
    father=models.CharField(max_length=20)
    Birthdate=models.CharField(max_length=30,default='')
    collage=models.CharField(max_length=30,default='')
    
    

    
    def __str__(self):
        return self.name
