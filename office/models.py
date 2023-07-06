from django.db import models

# Create your models here.
class office_register1(models.Model):
    id = models.AutoField(primary_key=True)
    officename = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    mobile = models.BigIntegerField()
    password = models.CharField(max_length=200)

class emppay_slip(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=300)
    uname = models.CharField(max_length=300)
    designation = models.CharField(max_length=300)
    month = models.CharField(max_length=300)
    year = models.CharField(max_length=300)
    basic_da = models.CharField(max_length=300)
    hra = models.CharField(max_length=300)
    conveyance = models.CharField(max_length=300)
    pf = models.CharField(max_length=300)
    esi = models.CharField(max_length=300)
    net_salary = models.CharField(max_length=300)

class salary_slip(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=300)
    uname = models.CharField(max_length=300)
    designation = models.CharField(max_length=300)
    month = models.CharField(max_length=300)
    year = models.CharField(max_length=300)
    basic_da = models.CharField(max_length=300)
    hra = models.CharField(max_length=300)
    conveyance = models.CharField(max_length=300)
    pf = models.CharField(max_length=300)
    esi = models.CharField(max_length=300)
    net_salary = models.CharField(max_length=300)
    file_path = models.CharField(max_length=300)
    phash1 = models.CharField(max_length=300)
    newhash1 = models.CharField(max_length=300)
    atimestamp = models.CharField(max_length=300)
    certificate_file = models.FileField()

class experience1(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=300)
    uname = models.CharField(max_length=300)
    designation = models.CharField(max_length=300)
    exp_year = models.CharField(max_length=300)
    starting_year = models.CharField(max_length=300)
    finishing_year = models.CharField(max_length=300)

class exp_certificate(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=300)
    uname = models.CharField(max_length=300)
    designation = models.CharField(max_length=300)
    exp_year = models.CharField(max_length=300)
    starting_year = models.CharField(max_length=300)
    finishing_year = models.CharField(max_length=300)
    file_path = models.CharField(max_length=300)
    phash1 = models.CharField(max_length=300)
    newhash1 = models.CharField(max_length=300)
    atimestamp = models.CharField(max_length=300)
    certificate_file = models.FileField()