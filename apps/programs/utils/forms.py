# Adminapp/utils/forms.py
from django import forms
from ..models import Departments, Program, Subject, Clubs,Batch
from bootstrap_datepicker_plus import DatePickerInput


# Add new department or Update
class ClubCreateForm(forms.ModelForm):
    class Meta:
        model = Clubs
        fields = "__all__"

        widgets = {
            'established_at': DatePickerInput()
        }


# Add new department or Update
class DeptCreateForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = "__all__"

        widgets = {
            'established_at': DatePickerInput()
        }


# Add new Program / Cources  or Update
class ProgramCreateForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = "__all__"

        widgets = {
            'established_at': DatePickerInput(), 'approved_on': DatePickerInput()
        }


# Add new Program / Cources  or Update
class BatchCreateForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = "__all__"

        widgets = {
            'established_at': DatePickerInput(), 'approved_on': DatePickerInput()
        }


# Add new Subject or Papers  or Update
class SubjectCreateForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"

        widgets = {
            'established_at': DatePickerInput(), 'approved_on': DatePickerInput()
        }

    def __init__(self, *args, **kwargs):
        #self.user = kwargs.pop('user')
        super(SubjectCreateForm, self).__init__(*args, **kwargs)

        self.fields['department'].queryset = Departments.objects.all()
        self.fields['program'].queryset = Program.objects.none()
        if 'program' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['program'].queryset = Program.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['program'].queryset = self.instance.department.program_set.order_by('name')
