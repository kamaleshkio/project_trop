# Generated by Django 2.0.5 on 2021-02-04 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_college_details1_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='college_details1',
            name='university',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]