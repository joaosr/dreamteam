from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    modified = models.DateTimeField('Modified', auto_now=True)
    def __str__(self):
        return self.name


class UserMember(models.Model):
    email = models.EmailField(max_length=30, primary_key=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    verifeid = models.BooleanField('Verifeid', default=False)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    modified = models.DateTimeField('Modified', auto_now=True)
