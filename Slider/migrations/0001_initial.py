# Generated by Django 3.1.5 on 2021-01-27 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('ShortText', models.TextField()),
                ('SliderImage', models.ImageField(upload_to='slider/')),
            ],
        ),
    ]
