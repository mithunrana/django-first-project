from django.db import models


class Slider2(models.Model):
    Name = models.CharField(max_length=250)
    ShortText = models.TextField()
    SliderImage = models.ImageField(upload_to='slider/',blank=False)

    def __str__(self):
        return self.Name
