# Generated by Django 2.0.5 on 2021-01-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('government', '0006_auto_20210123_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='community_certificate1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=300)),
                ('full_name', models.CharField(max_length=200)),
                ('dateof_birth', models.CharField(max_length=300)),
                ('religion', models.CharField(max_length=300)),
                ('caste', models.CharField(max_length=300)),
                ('father_name', models.CharField(max_length=300)),
                ('mother_name', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=300)),
                ('file_path', models.FileField(upload_to='')),
                ('phash1', models.CharField(max_length=300)),
                ('newhash1', models.CharField(max_length=300)),
                ('atimestamp', models.CharField(max_length=300)),
            ],
        ),
    ]
