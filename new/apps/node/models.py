from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Kit(models.Model):
    floor_name = models.CharField(max_length=10)
    light1_name=models.CharField(max_length=10)
    light1_status=models.CharField(max_length=10)
    light2_name=models.CharField(max_length=10)
    light2_status=models.CharField(max_length=10)
    light3_name=models.CharField(max_length=10)
    light3_status=models.CharField(max_length=10)

    def __str__(self):
        return self.floor_name
