# Programs/Models.py
from django.db import models
from django.contrib.auth import get_user_model
import uuid
import datetime

User = get_user_model()


# Create your models here.
class Departments(models.Model):
    name = models.CharField(max_length=30, unique=True)
    code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    description = models.TextField(max_length=300, null=True)
    status = models.BooleanField(default=False)
    established_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Clubs(models.Model):
    name = models.CharField(max_length=50, unique=True)
    user = models.ManyToManyField(User, related_name="club_user")
    code = models.CharField(max_length=10, null=True, blank=True, unique=True)
    description = models.TextField(max_length=300, null=True)
    status = models.BooleanField(default=False)
    established_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Program(models.Model):  # Cource
    department = models.ForeignKey('Departments', on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=30, unique=True)
    code = models.CharField(max_length=15, null=True, blank=True, unique=True)
    description = models.TextField(max_length=300, null=True)
    status = models.BooleanField(default=False)
    established_at = models.DateField()
    approved_on = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Subject(models.Model):  # Paper
    department = models.ForeignKey('Departments', on_delete=models.DO_NOTHING, null=True)
    program = models.ForeignKey('Program', on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=180)
    code = models.CharField(max_length=45, null=True, blank=True,)
    description = models.TextField(max_length=300, null=True)
    status = models.BooleanField(default=False)
    established_at = models.DateField()
    approved_on = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Batch(models.Model):
    name = models.CharField(max_length=12, null=True)
    batch_no = models.IntegerField(unique=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
