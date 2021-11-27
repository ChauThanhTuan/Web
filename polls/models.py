from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email

class Feedback(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = RichTextField()