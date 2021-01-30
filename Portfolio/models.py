from django.db import models

class portfolioCategory(models.Model):
    CategoryName = models.CharField(max_length=250)
    Permalink = models.CharField(max_length=250)
    MetaKeyword = models.TextField(max_length=250)
    MetaDescription = models.TextField(max_length=250)
    BrowserTitle = models.TextField(max_length=250)

    def __str__(self):
        return self.CategoryName


class portfolio(models.Model):
    ProjectName = models.CharField(max_length=250)
    Permalink = models.CharField(max_length=250)
    ProjectTitle = models.CharField(max_length=250)
    BrowserTitle = models.CharField(max_length=250)
    MetaKeyword = models.TextField(null=True)
    MetaDescription = models.TextField(null=True)
    CategoryName = models.ForeignKey(portfolioCategory, null=True, on_delete=models.SET_NULL)
    LiveUrl = models.CharField(max_length=250,null=True)
    SliderImage = models.ImageField(upload_to='portfolio/', blank=False)
    ImageTitleText = models.CharField(max_length=250,null=True)
    ImageAltText = models.CharField(max_length=250,null=True)
    ProjectDetails = models.TextField(null=True)
    ActiveStatus = models.IntegerField(default='0')

    def __str__(self):
        return self.ProjectName
        return self.ProjectTitle

