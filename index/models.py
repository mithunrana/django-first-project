from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class Slider(models.Model):
    Image = models.CharField(max_length=50)
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=50)