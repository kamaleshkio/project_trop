# Generated by Django 2.0.5 on 2021-02-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='emppay_slip',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=300)),
                ('uname', models.CharField(max_length=300)),
                ('designation', models.CharField(max_length=300)),
                ('month', models.CharField(max_length=300)),
                ('year', models.CharField(max_length=300)),
                ('basic_da', models.CharField(max_length=300)),
                ('hra', models.CharField(max_length=300)),
                ('conveyance', models.CharField(max_length=300)),
                ('pf', models.CharField(max_length=300)),
                ('esi', models.CharField(max_length=300)),
                ('net_salary', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='salary_slip',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=300)),
                ('uname', models.CharField(max_length=300)),
                ('designation', models.CharField(max_length=300)),
                ('month', models.CharField(max_length=300)),
                ('year', models.CharField(max_length=300)),
                ('basic_da', models.CharField(max_length=300)),
                ('hra', models.CharField(max_length=300)),
                ('conveyance', models.CharField(max_length=300)),
                ('pf', models.CharField(max_length=300)),
                ('esi', models.CharField(max_length=300)),
                ('net_salary', models.CharField(max_length=300)),
                ('file_path', models.FileField(upload_to='')),
                ('phash1', models.CharField(max_length=300)),
                ('newhash1', models.CharField(max_length=300)),
                ('atimestamp', models.CharField(max_length=300)),
            ],
        ),
    ]
