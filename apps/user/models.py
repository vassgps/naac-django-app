# User/Models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class AllUserScope():
    USER_SCOPES = [("ADMIN", "Admin"), ("NAAC_COD", "Naac Coordinator"), ("DEPT_COD", "Department"),
                   ("TEACHER", "Teacher"), ("CLUB", "Clubs"), ("STAFF", "Staff"), ("OTHER", "Other"), ]
    pass


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(blank=True, max_length=254, verbose_name="email address", unique=True)
    phone_number = models.CharField(max_length=15, null=True)
    designation = models.CharField(max_length=100, null=True, blank=True)
    department = models.ForeignKey('programs.Departments', null=True, on_delete=models.DO_NOTHING)
    user_scope = models.CharField(max_length=20, null=True, choices=AllUserScope.USER_SCOPES, default="CLUB")
    clubs = models.ForeignKey('programs.Clubs', related_name="user_clubs", null=True, blank=True,
                              on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False, verbose_name="Grand Permission to perform as a Teacher")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.username)
