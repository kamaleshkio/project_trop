from django.db import models

# Create your models here.
class gov_login(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=200)
    key1=models.CharField(max_length=200)

class bkey_request1(models.Model):
    id = models.AutoField(primary_key=True)
    requestor = models.CharField(max_length=300)
    person_name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    status1 = models.CharField(max_length=300)
    key1=models.CharField(max_length=300)

class birth_certificate1(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=300)
    gender = models.CharField(max_length=200)
    birth_place = models.CharField(max_length=300)
    dateof_birth = models.CharField(max_length=300)
    father_name=models.CharField(max_length=300)
    mother_name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    file_path = models.CharField(max_length=300)
    phash1=models.CharField(max_length=300)
    newhash1=models.CharField(max_length=300)
    atimestamp=models.CharField(max_length=300)
    certificate_file = models.FileField()

class community_certificate1(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=300)
    full_name = models.CharField(max_length=200)
    dateof_birth = models.CharField(max_length=300)
    religion = models.CharField(max_length=300)
    caste=models.CharField(max_length=300)
    father_name = models.CharField(max_length=300)
    mother_name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    file_path = models.CharField(max_length=300)
    phash1=models.CharField(max_length=300)
    newhash1=models.CharField(max_length=300)
    atimestamp=models.CharField(max_length=300)
    certificate_file = models.FileField()

class genration_card(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=300)
    full_name = models.CharField(max_length=200)
    dateof_birth = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    age=models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    member_count = models.CharField(max_length=300)
    file_path = models.CharField(max_length=300)
    phash1=models.CharField(max_length=300)
    newhash1=models.CharField(max_length=300)
    atimestamp=models.CharField(max_length=300)
    certificate_file = models.FileField()