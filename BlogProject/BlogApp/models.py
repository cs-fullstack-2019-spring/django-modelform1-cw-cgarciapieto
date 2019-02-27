from django.db import models
from django.utils import timezone
# model created for form fields
class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    created_date= models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
