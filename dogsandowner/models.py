from django.db import models

# Create your models here.
class Owner(models.Model):
    first_name = models.CharField(max_length=2)
    last_name = models.CharField(max_length=2)
    age = models.IntegerField()

    class Meta:
        db_table = 'owners'
        
        
class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    owner = models.ForeignKey('owner' , on_delete=models.CASCADE)
    
    
    class Meta:
        db_table = 'dogs'        
