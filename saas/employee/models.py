from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    email = models.CharField(max_length=100)
    address = models.TextField(max_length=200, null = True)
    department = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=50)

    def __str__(self):
        return

status_choices = (
    ('inside-building', 'Inside Building'),
    ('checked-out', 'checked-out'),
    ('check-in', 'check-in')

)

class Visitors(models.Model):
    email1 = models.CharField(max_length=100)
    name1 = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    status = models.CharField(max_length=100, choices=status_choices, null=True)
    guest = models.CharField(max_length=100, default="none")
    # guest = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return str(self.name1)
    # class Meta:
    #     ordering= ['name']



