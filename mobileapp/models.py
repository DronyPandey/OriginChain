from django.db import models

# Create your models here.
import uuid
from django.db import models
# from django.contrib.auth import models
from django.contrib.auth.models import AbstractUser



class Material(models.Model):
    material_id = models.CharField(max_length=32)
    property_1 = models.CharField(max_length=64)
    property_2 = models.CharField(max_length=64)
    property_3 = models.CharField(max_length=64)
    property_4 = models.CharField(max_length=64)
    property_5 = models.CharField(max_length=64)
    # def __str__(self):
    #     # desc = "%self.material_id, %self.material_id"
    #     return self.material_id


class MaterialTransaction(models.Model):
    user_id = models.CharField(max_length=32, default="default_user")
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    trans_type= models.CharField(max_length=1)
    trans_date = models.DateTimeField('Transaction Time')
    # def __str__(self):
    #     return self.user_id
