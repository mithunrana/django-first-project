# Generated by Django 2.2.10 on 2021-01-30 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0002_auto_20210130_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='CategoryName',
        ),
    ]
