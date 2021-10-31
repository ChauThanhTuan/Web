from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50, help_text='Ex: Mark Zuckerberg')
    email = models.EmailField(max_length=60, help_text='Ex: Mark@gmail.com')
    genderChoices = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    gender = models.CharField(max_length=1, choices=genderChoices, default='M')
    country = models.CharField(max_length=50, help_text='Ex: Vietnam')
    birthday = models.DateField()

    def __str__(self):
        return self.name