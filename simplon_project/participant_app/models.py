from django.db import models


# Create your models here.


class Participants(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.firstname
