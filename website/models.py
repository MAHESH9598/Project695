from django.db import models


# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=15)
    mobile_no = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
