# Generated by Django 2.0.5 on 2021-02-04 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='college_register1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('collegename', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=200)),
                ('mobile', models.BigIntegerField()),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
