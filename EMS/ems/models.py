from django.db import models

# Create your models here.
from django.db import models


class Employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    salary=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)

    def __str__(self):
        return self.name
