from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
# from django.contrib.auth.models import User

User = get_user_model()

# User Registration Form
class SignUpForm(UserCreationForm):
    password1 = forms.Field(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Password', 'required': 'required'}))
    password2 = forms.Field(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-type password', 'required': 'required'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email','phone_number','designation','department', 'password1', 'password2', )

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a Username or Staff ID', 'required': 'required'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number', 'required': 'required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': 'required'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Designation', 'blank':True }),
            'department': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Department', 'required': 'required'}),
            'user_scope': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Department', 'required': 'required'}),
            }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for field_name in ('email', 'username', 'password1', 'password2'):
            self.fields[field_name].help_text = ''

# User Profile Update Form
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
        'username', 'first_name', 'last_name', 'email', 'phone_number', 'designation', 'department', )


        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a Username or Staff ID',
                                               'required': 'required'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'First Name', 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Mobile Number', 'required': 'required'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Email Address', 'required': 'required'}),
            'designation': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Designation', 'blank': True}),
            'department': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Department', 'required': 'required'}),
            'user_scope': forms.Select(
                attrs={'class': 'form-control', 'placeholder': 'Department', 'required': 'required'}),
           }


# Change Password Form
class UpdatePasswordForm(PasswordChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('old_password', 'new_password1', 'new_password2')
        widgets = {
            'old_password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Current Password', 'type': 'password'}),
            'new_password1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a new Password', 'type': 'password'}),
            'new_password2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Re-type Password', 'type': 'password'}),

        }