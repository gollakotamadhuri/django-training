from unittest.util import _MAX_LENGTH

from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return "Name : {} {} ; Email : {}".format(self.first_name,
                                                  self.last_name, self.email)
