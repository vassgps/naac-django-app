#autoUpdate/urls.py
from django.urls import path
from .views import *
from .generator.create import *
from .generator.add_new_fields import *

app_name = 'autoUpdate'

urlpatterns = [
    path('', index, name="index"),
    path('create-tables', generate_tables, name="create-tables"),
    path('create-reports', generate_reports, name="create-reports"),
    path('data-entry', DataEntryForm.as_view(), name="data-entry"),
    path('update-home', PasswordValidator.as_view(), name="update-home"),
    path('show-fields', show_field_names, name="show-fields"),
    ]