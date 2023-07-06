# Generated by Django 2.0.5 on 2021-01-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='birth_details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('requestor', models.CharField(max_length=300)),
                ('person_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=300)),
                ('status1', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='gov_login',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=200)),
                ('key1', models.CharField(max_length=200)),
            ],
        ),
    ]