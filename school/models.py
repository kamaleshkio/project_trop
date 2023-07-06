from django.db import models

# Create your models here.
class school_register1(models.Model):
    id = models.AutoField(primary_key=True)
    schoolname = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    mobile = models.BigIntegerField()
    password = models.CharField(max_length=200)

class transfer_certificate1(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=300)
    full_name = models.CharField(max_length=200)
    dateof_birth = models.CharField(max_length=300)
    religion = models.CharField(max_length=300)
    caste=models.CharField(max_length=300)
    father_name = models.CharField(max_length=300)
    mother_name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    file_path = models.CharField(max_length=200)
    phash1=models.CharField(max_length=300)
    newhash1=models.CharField(max_length=300)
    atimestamp=models.CharField(max_length=300)
    sname = models.CharField(max_length=300)
    dateof_admission = models.CharField(max_length=300)
    last_studiedclass = models.CharField(max_length=300)
    reason_leaving = models.CharField(max_length=300)
    issue_date = models.CharField(max_length=300)
    general_conduct = models.CharField(max_length=300)
    certificate_file = models.FileField()

class attendance_details(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=300)
    sch_name = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)
    day = models.CharField(max_length=200)
    month = models.CharField(max_length=200)
    year = models.CharField(max_length=200)

class attendance_certificate1(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=300)
    sch_name = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)
    day = models.CharField(max_length=200)
    month = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    file_path =  models.CharField(max_length=200)
    phash1=models.CharField(max_length=300)
    newhash1=models.CharField(max_length=300)
    atimestamp=models.CharField(max_length=300)
    certificate_file = models.FileField()

class sports_details(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=300)
    sch_name = models.CharField(max_length=200)
    sports_name = models.CharField(max_length=200)
    winning_place = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

class sports_certificate1(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=300)
    sch_name = models.CharField(max_length=200)
    sports_name = models.CharField(max_length=200)
    winning_place = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    file_path =  models.CharField(max_length=200)
    phash1=models.CharField(max_length=300)
    newhash1=models.CharField(max_length=300)
    atimestamp=models.CharField(max_length=300)
    certificate_file = models.FileField()

class school_birth1(models.Model):
    id = models.AutoField(primary_key=True)
    requestor = models.CharField(max_length=300)
    studnet_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    certificate_name = models.CharField(max_length=200)
    status1 = models.CharField(max_length=200)
    key1 = models.CharField(max_length=200)