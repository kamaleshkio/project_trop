from django.db import models

# Create your models here.
class user_reg1(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    mobile = models.BigIntegerField()
    uname = models.CharField(max_length=300)
    password = models.CharField(max_length=200)

class community_details(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=300)
    uname = models.CharField(max_length=200)
    dateof_birth = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    religion = models.CharField(max_length=200)
    caste = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)

class ration_carddetails(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=300)
    uname = models.CharField(max_length=200)
    dateof_birth = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    age = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    member_count = models.CharField(max_length=200)


class school_details1(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=300)
    uname = models.CharField(max_length=200)
    dateof_birth = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    religion = models.CharField(max_length=200)
    caste = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    dateof_admission = models.CharField(max_length=200)
    last_studiedclass = models.CharField(max_length=200)
    reason_leaving = models.CharField(max_length=200)
    issue_date = models.CharField(max_length=200)
    general_conduct = models.CharField(max_length=200)
    school_name = models.CharField(max_length=200)

class college_details1(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=300)
    uname = models.CharField(max_length=200)
    dateof_birth = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    religion = models.CharField(max_length=200)
    caste = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    dateof_admission = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    joining_year = models.CharField(max_length=200)
    degree_finishingyear = models.CharField(max_length=200)
    college_name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    university = models.CharField(max_length=300)

class office_details(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=300)
    uname = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    designation = models.CharField(max_length=300)
