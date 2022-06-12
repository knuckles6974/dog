from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=30)
    dog = models.CharField(max_length=30)
    type = models.CharField(max_length=50)

    class Meta:
        db_table = 'owners'
