# Generated by Django 3.1.5 on 2021-01-26 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20210125_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.CharField(max_length=50)),
                ('Title', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=50)),
            ],
        ),
    ]
