# Generated by Django 2.0.5 on 2021-02-06 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('government', '0010_auto_20210206_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='community_certificate1',
            name='certificate_file',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='community_certificate1',
            name='file_path',
            field=models.CharField(max_length=300),
        ),
    ]