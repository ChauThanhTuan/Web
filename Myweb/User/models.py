from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50, help_text='Ex: Mark Zuckerberg')
    email = models.EmailField(max_length=60, help_text='Ex: Mark@gmail.com')
    password = models

    def __str__(self):
        return self.name