from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    project_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    project_photo_1=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    project_photo_2=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    project_photo_3=models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    url = models.URLField(max_length=200, blank=True)
    url_github = models.URLField(max_length=200, blank=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name
    