from django.db import models

# Create your models here.
class birth_details(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=300)
    gender = models.CharField(max_length=200)
    birth_place = models.CharField(max_length=300)
    dateof_birth = models.CharField(max_length=300)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

