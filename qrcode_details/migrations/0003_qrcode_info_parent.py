# Generated by Django 3.2.9 on 2022-05-08 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrcode_details', '0002_remove_qrcode_info_parentname'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode_info',
            name='parent',
            field=models.CharField(default='', max_length=40),
        ),
    ]