# Adminapp/forms.py
from django import forms
from .models import CriteriaManager
from django.contrib.auth import get_user_model
User = get_user_model()

class CriteriaForm(forms.ModelForm):
    class Meta:
        model = CriteriaManager
        exclude = ('status',)
        fields = "__all__"

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('status',)
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'designation',
                  'department',  'user_scope', 'is_verified', 'is_teacher', 'status',)