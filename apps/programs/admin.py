# Programs/Admin.py
from django.contrib import admin
from .models import Departments, Program, Subject, Batch, Clubs

# Register your models here.

admin.site.register(Departments)
admin.site.register(Program)
admin.site.register(Subject)
admin.site.register(Batch)
admin.site.register(Clubs)