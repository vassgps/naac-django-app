# Criteria/forms.py
import datetime
from django import forms
from .models import CriterionMaster
from ..programs.models import Departments, Program, Subject
from ..adminapp.models import FinalCriteria
from bootstrap_datepicker_plus import DatePickerInput
from .fields.field_names import *

# Define Global widgets

widget_dict = {
    'date': DatePickerInput(),
    'date2': DatePickerInput(),
    'date3': DatePickerInput(),
    'date4': DatePickerInput(),
    'date5': DatePickerInput(),
    'department': forms.Select(attrs={'class': 'form-control', 'required': False}),
    'batch': forms.Select(attrs={'class': 'form-control', 'required': False}),
    'program': forms.Select(attrs={'class': 'form-control', 'required': False}),
    'paper': forms.Select(attrs={'class': 'form-control', 'required': False}),
    'char1': forms.TextInput(attrs={'class': 'form-control', 'required': False, }),
    'char2': forms.TextInput(attrs={'class': 'form-control', 'required': False, }),
    'text1': forms.Textarea(
        attrs={'class': 'form-control', 'required': False, 'style': 'height: 70px;width:300px'}),
    'text2': forms.Textarea(
        attrs={'class': 'form-control', 'required': False, 'style': 'height: 70px;width:300px'}),
    'text3': forms.Textarea(
        attrs={'class': 'form-control', 'required': False, 'style': 'height: 70px;width:300px'}),
    'text4': forms.Textarea(
        attrs={'class': 'form-control', 'required': False, 'style': 'height: 70px;width:300px'}),
    'text5': forms.Textarea(
        attrs={'class': 'form-control', 'required': False, 'style': 'height: 70px;width:300px'}),
    'text6': forms.Textarea(
        attrs={'class': 'form-control', 'required': False, 'style': 'height: 70px;width:300px'}),
    'text7': forms.Textarea(
        attrs={'class': 'form-control', 'required': False, 'style': 'height: 70px;width:300px'}),
    'text8': forms.Textarea(
        attrs={'class': 'form-control', 'required': False, 'style': 'height: 70px;width:300px'}),
    'text9': forms.Textarea(
        attrs={'class': 'form-control', 'required': False, 'style': 'height: 70px;width:300px'}),
    'text10': forms.Textarea(
        attrs={'class': 'form-control', 'required': False, 'style': 'height: 70px;width:300px'}),
    'text11': forms.Textarea(
        attrs={'class': 'form-control', 'required': False, 'style': 'height: 70px;width:300px'}),
    'text12': forms.Textarea(
        attrs={'class': 'form-control', 'required': False, 'style': 'height: 70px;width:300px'}),
    'text13': forms.Textarea(
        attrs={'class': 'form-control', 'required': False, 'style': 'height: 70px;width:300px'}),
    'text14': forms.Textarea(
        attrs={'class': 'form-control', 'required': False, 'style': 'height: 70px;width:300px'}),
    'text15': forms.Textarea(
        attrs={'class': 'form-control', 'required': False, 'style': 'height: 70px;width:300px'}),

}


# ------------------------* Forms for Criteria 1.1.1 * -------------------------------- #
class C1_1_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_1_1
        labels = dc1_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_1_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_1_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_1_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_1_1


# Update Form
class C1_1_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_1_1
        labels = dc1_1_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_1_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_1_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_1_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_1_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1.1.2 * -------------------------------- #
class C1_1_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_1_2
        labels = dc1_1_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_1_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_1_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_1_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_1_2


# Update Form
class C1_1_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_1_2
        labels = dc1_1_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_1_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_1_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_1_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_1_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_1_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


class C1_1_3CreateForm(forms.ModelForm):
    CHOICES = (('Employability', 'Employability'), ('Entrepreneurship', 'Entrepreneurship'),
               ('Skill development', 'Skill development'))
    text3 = forms.ChoiceField(choices=CHOICES, label="Focus of the activity")

    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_1_3
        labels = dc1_1_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_1_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_1_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_1_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_1_3


# Update Form
class C1_1_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_1_3
        labels = dc1_1_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_1_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_1_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_1_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_1_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_1_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1.2.1 * -------------------------------- #
class C1_2_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_2_1
        labels = dc1_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_2_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_2_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_2_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_2_1


# Update Form
class C1_2_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_2_1
        labels = dc1_2_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_2_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_2_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_2_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_2_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1.2.2 * -------------------------------- #
class C1_2_2CreateForm(forms.ModelForm):
    CHOICES = (('CBCS', 'CBCS'), ('ELECTIVE', 'Elective'),)
    text2 = forms.ChoiceField(choices=CHOICES, label="Type of Course")

    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_2_2
        labels = dc1_2_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_2_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_2_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_2_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_2_2


# Update Form
class C1_2_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_2_2
        labels = dc1_2_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_2_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_2_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_2_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_2_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_2_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1.3.1 * -------------------------------- #
class C1_3_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_3_1
        labels = dc1_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_3_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_3_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_3_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_3_1


# Update Form
class C1_3_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_3_1
        labels = dc1_3_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_3_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_3_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_3_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_3_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1.3.2 * -------------------------------- #
class C1_3_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_3_2
        labels = dc1_3_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_3_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_3_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_3_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_3_2


# Update Form
class C1_3_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_3_2
        labels = dc1_3_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_3_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_3_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_3_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_3_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_3_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1.3.3 * -------------------------------- #
class C1_3_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_3_3
        labels = dc1_3_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_3_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_3_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_3_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_3_3


# Update Form
class C1_3_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_3_3
        labels = dc1_3_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_3_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_3_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_3_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_3_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_3_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1.3.4 * -------------------------------- #
class C1_3_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_3_4
        labels = dc1_3_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_3_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_3_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_3_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_3_4


# Update Form
class C1_3_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_3_4
        labels = dc1_3_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_3_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_3_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_3_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_3_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_3_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1.4.1 * -------------------------------- #
class C1_4_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_4_1
        labels = dc1_4_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_4_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_4_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_4_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_4_1


# Update Form
class C1_4_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_4_1
        labels = dc1_4_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_4_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_4_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_4_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_4_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_4_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 1.4.2 * -------------------------------- #
class C1_4_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_4_2
        labels = dc1_4_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c1_4_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c1_4_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C1_4_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc1_4_2


# Update Form
class C1_4_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc1_4_2
        labels = dc1_4_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C1_4_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C1_4_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C1_4_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc1_4_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C1_4_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_1_1 * -------------------------------- #
class C2_1_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_1_1
        labels = dc2_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_1_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_1_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_1_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')
    def field_data(self, *args, **kwargs):
        field_tuple = fc2_1_1


# Update Form
class C2_1_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_1_1
        labels = dc2_1_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_1_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_1_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_1_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_1_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_1_2 * -------------------------------- #
class C2_1_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_1_2
        labels = dc2_1_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_1_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_1_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_1_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_1_2


# Update Form
class C2_1_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_1_2
        labels = dc2_1_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_1_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_1_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_1_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_1_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_1_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_1_3 * -------------------------------- #
class C2_1_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_1_3
        labels = dc2_1_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_1_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_1_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_1_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_1_3


# Update Form
class C2_1_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_1_3
        labels = dc2_1_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_1_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_1_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_1_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_1_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_1_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_2_1 * -------------------------------- #
class C2_2_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_2_1
        labels = dc2_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_2_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_2_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_2_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_2_1


# Update Form
class C2_2_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_2_1
        labels = dc2_2_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_2_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_2_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_2_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_2_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_2_2 * -------------------------------- #
class C2_2_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_2_2
        labels = dc2_2_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_2_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_2_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_2_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_2_2


# Update Form
class C2_2_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_2_2
        labels = dc2_2_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_2_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_2_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_2_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_2_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_2_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_2_3 * -------------------------------- #
class C2_2_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_2_3
        labels = dc2_2_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_2_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_2_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_2_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_2_3


# Update Form
class C2_2_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_2_3
        labels = dc2_2_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_2_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_2_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_2_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_2_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_2_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_3_1 * -------------------------------- #
class C2_3_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_3_1
        labels = dc2_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_3_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_3_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_3_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_3_1


# Update Form
class C2_3_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_3_1
        labels = dc2_3_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_3_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_3_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_3_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_3_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_3_2 * -------------------------------- #
class C2_3_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_3_2
        labels = dc2_3_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_3_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_3_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_3_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_3_2


# Update Form
class C2_3_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_3_2
        labels = dc2_3_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_3_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_3_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_3_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_3_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_3_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_3_3 * -------------------------------- #
class C2_3_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_3_3
        labels = dc2_3_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_3_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_3_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_3_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_3_3


# Update Form
class C2_3_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_3_3
        labels = dc2_3_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_3_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_3_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_3_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_3_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_3_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_3_4 * -------------------------------- #
class C2_3_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_3_4
        labels = dc2_3_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_3_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_3_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_3_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_3_4


# Update Form
class C2_3_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_3_4
        labels = dc2_3_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_3_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_3_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_3_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_3_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_3_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_4_1 * -------------------------------- #
class C2_4_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_1
        labels = dc2_4_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_4_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_4_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_4_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_4_1


# Update Form
class C2_4_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_1
        labels = dc2_4_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_4_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_4_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_4_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_4_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_4_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_4_2 * -------------------------------- #
class C2_4_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_2
        labels = dc2_4_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_4_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_4_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_4_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_4_2


# Update Form
class C2_4_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_2
        labels = dc2_4_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_4_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_4_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_4_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_4_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_4_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_4_3 * -------------------------------- #
class C2_4_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_3
        labels = dc2_4_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_4_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_4_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_4_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_4_3


# Update Form
class C2_4_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_3
        labels = dc2_4_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_4_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_4_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_4_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_4_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_4_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_4_4 * -------------------------------- #
class C2_4_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_4
        labels = dc2_4_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_4_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_4_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_4_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_4_4


# Update Form
class C2_4_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_4
        labels = dc2_4_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_4_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_4_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_4_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_4_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_4_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_4_5 * -------------------------------- #
class C2_4_5CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_5
        labels = dc2_4_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_4_5')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_4_5'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_4_5CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_4_5


# Update Form
class C2_4_5UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_4_5
        labels = dc2_4_5
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_4_5UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_4_5UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_4_5SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_4_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_4_5SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_5_1 * -------------------------------- #
class C2_5_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_1
        labels = dc2_5_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_5_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_5_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_5_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_5_1


# Update Form
class C2_5_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_1
        labels = dc2_5_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_5_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_5_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_5_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_5_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_5_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_5_2 * -------------------------------- #
class C2_5_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_2
        labels = dc2_5_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_5_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_5_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_5_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_5_2


# Update Form
class C2_5_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_2
        labels = dc2_5_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_5_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_5_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_5_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_5_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_5_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_5_3 * -------------------------------- #
class C2_5_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_3
        labels = dc2_5_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_5_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_5_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_5_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_5_3


# Update Form
class C2_5_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_3
        labels = dc2_5_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_5_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_5_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_5_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_5_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_5_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_5_4 * -------------------------------- #
class C2_5_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_4
        labels = dc2_5_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_5_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_5_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_5_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_5_4


# Update Form
class C2_5_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_4
        labels = dc2_5_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_5_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_5_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_5_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_5_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_5_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_5_5 * -------------------------------- #
class C2_5_5CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_5
        labels = dc2_5_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_5_5')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_5_5'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_5_5CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_5_5


# Update Form
class C2_5_5UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_5_5
        labels = dc2_5_5
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_5_5UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_5_5UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_5_5SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_5_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_5_5SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_6_1 * -------------------------------- #
class C2_6_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_6_1
        labels = dc2_6_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_6_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_6_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_6_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_6_1


# Update Form
class C2_6_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_6_1
        labels = dc2_6_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_6_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_6_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_6_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_6_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_6_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_6_2 * -------------------------------- #
class C2_6_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_6_2
        labels = dc2_6_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_6_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_6_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_6_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_6_2


# Update Form
class C2_6_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_6_2
        labels = dc2_6_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_6_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_6_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_6_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_6_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_6_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_6_3 * -------------------------------- #
class C2_6_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_6_3
        labels = dc2_6_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_6_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_6_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_6_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_6_3


# Update Form
class C2_6_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_6_3
        labels = dc2_6_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_6_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_6_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_6_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_6_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_6_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 2_7_1 * -------------------------------- #
class C2_7_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_7_1
        labels = dc2_7_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c2_7_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c2_7_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C2_7_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc2_7_1


# Update Form
class C2_7_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc2_7_1
        labels = dc2_7_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C2_7_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C2_7_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C2_7_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc2_7_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C2_7_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_1_1 * -------------------------------- #
class C3_1_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_1_1
        labels = dc3_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_1_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_1_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_1_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_1_1


# Update Form
class C3_1_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_1_1
        labels = dc3_1_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_1_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_1_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_1_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_1_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_1_2 * -------------------------------- #
class C3_1_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_1_2
        labels = dc3_1_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_1_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_1_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_1_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_1_2


# Update Form
class C3_1_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_1_2
        labels = dc3_1_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_1_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_1_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_1_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_1_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_1_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_1_3 * -------------------------------- #
class C3_1_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_1_3
        labels = dc3_1_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_1_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_1_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_1_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_1_3


# Update Form
class C3_1_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_1_3
        labels = dc3_1_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_1_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_1_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_1_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_1_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_1_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_1_4 * -------------------------------- #
class C3_1_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_1_4
        labels = dc3_1_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_1_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_1_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_1_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_1_4


# Update Form
class C3_1_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_1_4
        labels = dc3_1_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_1_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_1_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_1_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_1_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_1_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_2_1 * -------------------------------- #
class C3_2_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_2_1
        labels = dc3_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_2_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_2_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_2_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_2_1


# Update Form
class C3_2_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_2_1
        labels = dc3_2_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_2_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_2_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_2_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_2_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_2_2 * -------------------------------- #
class C3_2_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_2_2
        labels = dc3_2_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_2_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_2_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_2_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_2_2


# Update Form
class C3_2_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_2_2
        labels = dc3_2_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_2_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_2_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_2_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_2_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_2_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_2_3 * -------------------------------- #
class C3_2_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_2_3
        labels = dc3_2_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_2_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_2_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_2_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_2_3


# Update Form
class C3_2_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_2_3
        labels = dc3_2_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_2_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_2_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_2_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_2_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_2_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_2_4 * -------------------------------- #
class C3_2_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_2_4
        labels = dc3_2_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_2_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_2_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_2_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_2_4


# Update Form
class C3_2_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_2_4
        labels = dc3_2_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_2_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_2_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_2_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_2_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_2_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_3_1 * -------------------------------- #
class C3_3_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_3_1
        labels = dc3_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_3_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_3_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_3_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_3_1


# Update Form
class C3_3_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_3_1
        labels = dc3_3_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_3_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_3_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_3_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_3_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_3_2 * -------------------------------- #
class C3_3_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_3_2
        labels = dc3_3_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_3_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_3_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_3_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_3_2


# Update Form
class C3_3_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_3_2
        labels = dc3_3_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_3_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_3_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_3_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_3_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_3_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_3_3 * -------------------------------- #
class C3_3_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_3_3
        labels = dc3_3_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_3_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_3_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_3_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_3_3


# Update Form
class C3_3_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_3_3
        labels = dc3_3_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_3_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_3_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_3_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_3_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_3_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_4_1 * -------------------------------- #
class C3_4_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_4_1
        labels = dc3_4_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_4_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_4_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_4_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_4_1


# Update Form
class C3_4_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_4_1
        labels = dc3_4_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_4_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_4_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_4_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_4_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_4_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_4_2 * -------------------------------- #
class C3_4_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_4_2
        labels = dc3_4_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_4_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_4_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_4_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_4_2


# Update Form
class C3_4_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_4_2
        labels = dc3_4_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_4_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_4_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_4_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_4_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_4_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_4_3 * -------------------------------- #
class C3_4_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_4_3
        labels = dc3_4_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_4_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_4_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_4_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_4_3


# Update Form
class C3_4_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_4_3
        labels = dc3_4_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_4_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_4_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_4_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_4_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_4_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_4_4 * -------------------------------- #
class C3_4_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_4_4
        labels = dc3_4_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_4_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_4_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_4_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_4_4


# Update Form
class C3_4_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_4_4
        labels = dc3_4_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_4_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_4_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_4_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_4_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_4_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_4_5 * -------------------------------- #
class C3_4_5CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_4_5
        labels = dc3_4_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_4_5')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_4_5'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_4_5CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_4_5


# Update Form
class C3_4_5UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_4_5
        labels = dc3_4_5
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_4_5UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_4_5UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_4_5SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_4_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_4_5SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_4_6 * -------------------------------- #
class C3_4_6CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_4_6
        labels = dc3_4_6
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_4_6')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_4_6'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_4_6CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_4_6


# Update Form
class C3_4_6UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_4_6
        labels = dc3_4_6
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_4_6UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_4_6UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_4_6SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_4_6
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_4_6SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_4_7 * -------------------------------- #
class C3_4_7CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_4_7
        labels = dc3_4_7
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_4_7')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_4_7'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_4_7CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_4_7


# Update Form
class C3_4_7UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_4_7
        labels = dc3_4_7
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_4_7UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_4_7UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_4_7SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_4_7
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_4_7SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_4_8 * -------------------------------- #
class C3_4_8CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_4_8
        labels = dc3_4_8
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_4_8')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_4_8'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_4_8CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_4_8


# Update Form
class C3_4_8UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_4_8
        labels = dc3_4_8
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_4_8UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_4_8UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_4_8SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_4_8
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_4_8SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_5_1 * -------------------------------- #
class C3_5_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_5_1
        labels = dc3_5_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_5_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_5_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_5_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_5_1


# Update Form
class C3_5_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_5_1
        labels = dc3_5_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_5_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_5_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_5_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_5_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_5_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_5_2 * -------------------------------- #
class C3_5_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_5_2
        labels = dc3_5_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_5_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_5_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_5_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_5_2


# Update Form
class C3_5_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_5_2
        labels = dc3_5_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_5_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_5_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_5_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_5_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_5_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_5_3 * -------------------------------- #
class C3_5_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_5_3
        labels = dc3_5_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_5_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_5_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_5_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_5_3


# Update Form
class C3_5_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_5_3
        labels = dc3_5_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_5_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_5_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_5_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_5_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_5_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_6_1 * -------------------------------- #
class C3_6_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_6_1
        labels = dc3_6_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_6_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_6_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_6_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_6_1


# Update Form
class C3_6_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_6_1
        labels = dc3_6_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_6_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_6_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_6_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_6_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_6_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_6_2 * -------------------------------- #
class C3_6_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_6_2
        labels = dc3_6_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_6_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_6_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_6_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_6_2


# Update Form
class C3_6_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_6_2
        labels = dc3_6_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_6_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_6_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_6_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_6_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_6_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_6_3 * -------------------------------- #
class C3_6_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_6_3
        labels = dc3_6_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_6_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_6_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_6_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_6_3


# Update Form
class C3_6_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_6_3
        labels = dc3_6_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_6_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_6_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_6_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_6_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_6_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_6_4 * -------------------------------- #
class C3_6_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_6_4
        labels = dc3_6_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_6_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_6_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_6_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_6_4


# Update Form
class C3_6_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_6_4
        labels = dc3_6_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_6_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_6_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_6_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_6_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_6_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_7_1 * -------------------------------- #
class C3_7_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_7_1
        labels = dc3_7_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_7_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_7_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_7_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_7_1


# Update Form
class C3_7_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_7_1
        labels = dc3_7_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_7_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_7_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_7_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_7_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_7_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_7_2 * -------------------------------- #
class C3_7_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_7_2
        labels = dc3_7_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_7_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_7_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_7_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_7_2


# Update Form
class C3_7_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_7_2
        labels = dc3_7_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_7_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_7_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_7_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_7_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_7_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 3_7_3 * -------------------------------- #
class C3_7_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_7_3
        labels = dc3_7_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c3_7_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c3_7_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C3_7_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc3_7_3


# Update Form
class C3_7_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc3_7_3
        labels = dc3_7_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C3_7_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C3_7_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C3_7_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc3_7_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C3_7_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_1_1 * -------------------------------- #
class C4_1_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_1_1
        labels = dc4_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_1_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_1_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_1_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_1_1


# Update Form
class C4_1_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_1_1
        labels = dc4_1_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_1_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_1_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_1_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_1_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_1_2A * -------------------------------- #
class C4_1_2ACreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_1_2A
        labels = dc4_1_2A
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_1_2A')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_1_2A'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_1_2ACreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_1_2A


# Update Form
class C4_1_2AUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_1_2A
        labels = dc4_1_2A
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_1_2AUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_1_2AUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_1_2ASearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_1_2A
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_1_2ASearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_1_2B * -------------------------------- #
class C4_1_2BCreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_1_2B
        labels = dc4_1_2B
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_1_2B')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_1_2B'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_1_2BCreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_1_2B


# Update Form
class C4_1_2BUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_1_2B
        labels = dc4_1_2B
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_1_2BUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_1_2BUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_1_2BSearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_1_2B
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_1_2BSearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_1_2C * -------------------------------- #
class C4_1_2CCreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_1_2C
        labels = dc4_1_2C
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_1_2C')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_1_2C'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_1_2CCreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_1_2C


# Update Form
class C4_1_2CUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_1_2C
        labels = dc4_1_2C
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_1_2CUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_1_2CUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_1_2CSearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_1_2C
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_1_2CSearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_1_2D * -------------------------------- #
class C4_1_2DCreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_1_2D
        labels = dc4_1_2D
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_1_2D')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_1_2D'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_1_2DCreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_1_2D


# Update Form
class C4_1_2DUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_1_2D
        labels = dc4_1_2D
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_1_2DUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_1_2DUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_1_2DSearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_1_2D
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_1_2DSearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_1_2E * -------------------------------- #
class C4_1_2ECreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_1_2E
        labels = dc4_1_2E
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_1_2E')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_1_2E'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_1_2ECreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_1_2E


# Update Form
class C4_1_2EUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_1_2E
        labels = dc4_1_2E
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_1_2EUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_1_2EUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_1_2ESearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_1_2E
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_1_2ESearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_1_3 * -------------------------------- #
class C4_1_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_1_3
        labels = dc4_1_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_1_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_1_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_1_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_1_3


# Update Form
class C4_1_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_1_3
        labels = dc4_1_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_1_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_1_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_1_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_1_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_1_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_1_4 * -------------------------------- #
class C4_1_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_1_4
        labels = dc4_1_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_1_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_1_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_1_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_1_4


# Update Form
class C4_1_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_1_4
        labels = dc4_1_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_1_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_1_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_1_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_1_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_1_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_2_1 * -------------------------------- #
class C4_2_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_2_1
        labels = dc4_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_2_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_2_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_2_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_2_1


# Update Form
class C4_2_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_2_1
        labels = dc4_2_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_2_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_2_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_2_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_2_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_2_2 * -------------------------------- #
class C4_2_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_2_2
        labels = dc4_2_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_2_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_2_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_2_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_2_2


# Update Form
class C4_2_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_2_2
        labels = dc4_2_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_2_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_2_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_2_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_2_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_2_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_2_3 * -------------------------------- #
class C4_2_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_2_3
        labels = dc4_2_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_2_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_2_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_2_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_2_3


# Update Form
class C4_2_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_2_3
        labels = dc4_2_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_2_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_2_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_2_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_2_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_2_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_2_4 * -------------------------------- #
class C4_2_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_2_4
        labels = dc4_2_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_2_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_2_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_2_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_2_4


# Update Form
class C4_2_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_2_4
        labels = dc4_2_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_2_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_2_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_2_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_2_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_2_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_2_5 * -------------------------------- #
class C4_2_5CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_2_5
        labels = dc4_2_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_2_5')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_2_5'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_2_5CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_2_5


# Update Form
class C4_2_5UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_2_5
        labels = dc4_2_5
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_2_5UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_2_5UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_2_5SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_2_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_2_5SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_2_6 * -------------------------------- #
class C4_2_6CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_2_6
        labels = dc4_2_6
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_2_6')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_2_6'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_2_6CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_2_6


# Update Form
class C4_2_6UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_2_6
        labels = dc4_2_6
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_2_6UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_2_6UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_2_6SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_2_6
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_2_6SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_3_1 * -------------------------------- #
class C4_3_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_3_1
        labels = dc4_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_3_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_3_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_3_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_3_1


# Update Form
class C4_3_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_3_1
        labels = dc4_3_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_3_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_3_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_3_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_3_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_3_2 * -------------------------------- #
class C4_3_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_3_2
        labels = dc4_3_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_3_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_3_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_3_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_3_2


# Update Form
class C4_3_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_3_2
        labels = dc4_3_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_3_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_3_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_3_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_3_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_3_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_3_3 * -------------------------------- #
class C4_3_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_3_3
        labels = dc4_3_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_3_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_3_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_3_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_3_3


# Update Form
class C4_3_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_3_3
        labels = dc4_3_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_3_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_3_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_3_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_3_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_3_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_3_4 * -------------------------------- #
class C4_3_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_3_4
        labels = dc4_3_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_3_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_3_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_3_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_3_4


# Update Form
class C4_3_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_3_4
        labels = dc4_3_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_3_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_3_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_3_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_3_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_3_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_4_1 * -------------------------------- #
class C4_4_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_4_1
        labels = dc4_4_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_4_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_4_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_4_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_4_1


# Update Form
class C4_4_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_4_1
        labels = dc4_4_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_4_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_4_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_4_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_4_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_4_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 4_4_2 * -------------------------------- #
class C4_4_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_4_2
        labels = dc4_4_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c4_4_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c4_4_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C4_4_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc4_4_2


# Update Form
class C4_4_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc4_4_2
        labels = dc4_4_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C4_4_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C4_4_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C4_4_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc4_4_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C4_4_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_1_1 * -------------------------------- #
class C5_1_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_1
        labels = dc5_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_1_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_1_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_1_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_1_1


# Update Form
class C5_1_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_1
        labels = dc5_1_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_1_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_1_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_1_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_1_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_1_2 * -------------------------------- #
class C5_1_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_2
        labels = dc5_1_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_1_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_1_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_1_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_1_2


# Update Form
class C5_1_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_2
        labels = dc5_1_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_1_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_1_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_1_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_1_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_1_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_1_3A * -------------------------------- #
class C5_1_3ACreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_3A
        labels = dc5_1_3A
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_1_3A')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_1_3A'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_1_3ACreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_1_3A


# Update Form
class C5_1_3AUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_3A
        labels = dc5_1_3A
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_1_3AUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_1_3AUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_1_3ASearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_1_3A
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_1_3ASearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_1_3B * -------------------------------- #
class C5_1_3BCreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_3B
        labels = dc5_1_3B
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_1_3B')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_1_3B'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_1_3BCreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_1_3B


# Update Form
class C5_1_3BUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_3B
        labels = dc5_1_3B
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_1_3BUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_1_3BUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_1_3BSearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_1_3B
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_1_3BSearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_1_3C * -------------------------------- #
class C5_1_3CCreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_3C
        labels = dc5_1_3C
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_1_3C')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_1_3C'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_1_3CCreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_1_3C


# Update Form
class C5_1_3CUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_3C
        labels = dc5_1_3C
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_1_3CUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_1_3CUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_1_3CSearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_1_3C
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_1_3CSearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_1_3D * -------------------------------- #
class C5_1_3DCreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_3D
        labels = dc5_1_3D
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_1_3D')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_1_3D'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_1_3DCreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_1_3D


# Update Form
class C5_1_3DUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_3D
        labels = dc5_1_3D
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_1_3DUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_1_3DUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_1_3DSearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_1_3D
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_1_3DSearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_1_3E * -------------------------------- #
class C5_1_3ECreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_3E
        labels = dc5_1_3E
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_1_3E')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_1_3E'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_1_3ECreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_1_3E


# Update Form
class C5_1_3EUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_3E
        labels = dc5_1_3E
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_1_3EUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_1_3EUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_1_3ESearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_1_3E
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_1_3ESearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_1_3F * -------------------------------- #
class C5_1_3FCreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_3F
        labels = dc5_1_3F
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_1_3F')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_1_3F'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_1_3FCreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_1_3F


# Update Form
class C5_1_3FUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_3F
        labels = dc5_1_3F
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_1_3FUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_1_3FUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_1_3FSearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_1_3F
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_1_3FSearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_1_3G * -------------------------------- #
class C5_1_3GCreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_3G
        labels = dc5_1_3G
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_1_3G')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_1_3G'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_1_3GCreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_1_3G


# Update Form
class C5_1_3GUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_3G
        labels = dc5_1_3G
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_1_3GUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_1_3GUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_1_3GSearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_1_3G
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_1_3GSearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_1_3H * -------------------------------- #
class C5_1_3HCreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_3H
        labels = dc5_1_3H
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_1_3H')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_1_3H'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_1_3HCreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_1_3H


# Update Form
class C5_1_3HUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_3H
        labels = dc5_1_3H
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_1_3HUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_1_3HUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_1_3HSearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_1_3H
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_1_3HSearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_1_4 * -------------------------------- #
class C5_1_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_4
        labels = dc5_1_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_1_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_1_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_1_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_1_4


# Update Form
class C5_1_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_4
        labels = dc5_1_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_1_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_1_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_1_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_1_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_1_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_1_5 * -------------------------------- #
class C5_1_5CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_5
        labels = dc5_1_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_1_5')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_1_5'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_1_5CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_1_5


# Update Form
class C5_1_5UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_5
        labels = dc5_1_5
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_1_5UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_1_5UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_1_5SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_1_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_1_5SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_1_6 * -------------------------------- #
class C5_1_6CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_6
        labels = dc5_1_6
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_1_6')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_1_6'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_1_6CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_1_6


# Update Form
class C5_1_6UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_1_6
        labels = dc5_1_6
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_1_6UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_1_6UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_1_6SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_1_6
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_1_6SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_2_1 * -------------------------------- #
class C5_2_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_2_1
        labels = dc5_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_2_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_2_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_2_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_2_1


# Update Form
class C5_2_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_2_1
        labels = dc5_2_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_2_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_2_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_2_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_2_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_2_2 * -------------------------------- #
class C5_2_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_2_2
        labels = dc5_2_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_2_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_2_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_2_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_2_2


# Update Form
class C5_2_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_2_2
        labels = dc5_2_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_2_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_2_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_2_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_2_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_2_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_2_3 * -------------------------------- #
class C5_2_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_2_3
        labels = dc5_2_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_2_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_2_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_2_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_2_3


# Update Form
class C5_2_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_2_3
        labels = dc5_2_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_2_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_2_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_2_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_2_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_2_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_3_1 * -------------------------------- #
class C5_3_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_3_1
        labels = dc5_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_3_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_3_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_3_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_3_1


# Update Form
class C5_3_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_3_1
        labels = dc5_3_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_3_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_3_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_3_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_3_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_3_2A * -------------------------------- #
class C5_3_2ACreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_3_2A
        labels = dc5_3_2A
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_3_2A')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_3_2A'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_3_2ACreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_3_2A


# Update Form
class C5_3_2AUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_3_2A
        labels = dc5_3_2A
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_3_2AUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_3_2AUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_3_2ASearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_3_2A
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_3_2ASearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_3_2B * -------------------------------- #
class C5_3_2BCreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_3_2B
        labels = dc5_3_2B
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_3_2B')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_3_2B'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_3_2BCreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_3_2B


# Update Form
class C5_3_2BUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_3_2B
        labels = dc5_3_2B
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_3_2BUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_3_2BUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_3_2BSearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_3_2B
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_3_2BSearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_3_3 * -------------------------------- #
class C5_3_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_3_3
        labels = dc5_3_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_3_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_3_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_3_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_3_3


# Update Form
class C5_3_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_3_3
        labels = dc5_3_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_3_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_3_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_3_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_3_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_3_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_4_1A * -------------------------------- #
class C5_4_1ACreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_4_1A
        labels = dc5_4_1A
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_4_1A')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_4_1A'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_4_1ACreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_4_1A


# Update Form
class C5_4_1AUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_4_1A
        labels = dc5_4_1A
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_4_1AUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_4_1AUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_4_1ASearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_4_1A
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_4_1ASearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_4_1B * -------------------------------- #
class C5_4_1BCreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_4_1B
        labels = dc5_4_1B
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_4_1B')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_4_1B'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_4_1BCreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_4_1B


# Update Form
class C5_4_1BUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_4_1B
        labels = dc5_4_1B
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_4_1BUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_4_1BUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_4_1BSearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_4_1B
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_4_1BSearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 5_4_2 * -------------------------------- #
class C5_4_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_4_2
        labels = dc5_4_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c5_4_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c5_4_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C5_4_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc5_4_2


# Update Form
class C5_4_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc5_4_2
        labels = dc5_4_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C5_4_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C5_4_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C5_4_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc5_4_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C5_4_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_1_1 * -------------------------------- #
class C6_1_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_1_1
        labels = dc6_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_1_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_1_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_1_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_1_1


# Update Form
class C6_1_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_1_1
        labels = dc6_1_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_1_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_1_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_1_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_1_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_1_2 * -------------------------------- #
class C6_1_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_1_2
        labels = dc6_1_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_1_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_1_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_1_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_1_2


# Update Form
class C6_1_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_1_2
        labels = dc6_1_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_1_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_1_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_1_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_1_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_1_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_2_1 * -------------------------------- #
class C6_2_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_2_1
        labels = dc6_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_2_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_2_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_2_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_2_1


# Update Form
class C6_2_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_2_1
        labels = dc6_2_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_2_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_2_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_2_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_2_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_2_2 * -------------------------------- #
class C6_2_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_2_2
        labels = dc6_2_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_2_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_2_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_2_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_2_2


# Update Form
class C6_2_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_2_2
        labels = dc6_2_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_2_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_2_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_2_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_2_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_2_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_2_3 * -------------------------------- #
class C6_2_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_2_3
        labels = dc6_2_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_2_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_2_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_2_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_2_3


# Update Form
class C6_2_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_2_3
        labels = dc6_2_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_2_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_2_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_2_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_2_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_2_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_2_4 * -------------------------------- #
class C6_2_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_2_4
        labels = dc6_2_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_2_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_2_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_2_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_2_4


# Update Form
class C6_2_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_2_4
        labels = dc6_2_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_2_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_2_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_2_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_2_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_2_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_3_1 * -------------------------------- #
class C6_3_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_3_1
        labels = dc6_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_3_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_3_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_3_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_3_1


# Update Form
class C6_3_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_3_1
        labels = dc6_3_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_3_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_3_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_3_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_3_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_3_2 * -------------------------------- #
class C6_3_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_3_2
        labels = dc6_3_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_3_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_3_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_3_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_3_2


# Update Form
class C6_3_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_3_2
        labels = dc6_3_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_3_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_3_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_3_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_3_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_3_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_3_3 * -------------------------------- #
class C6_3_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_3_3
        labels = dc6_3_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_3_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_3_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_3_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_3_3


# Update Form
class C6_3_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_3_3
        labels = dc6_3_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_3_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_3_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_3_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_3_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_3_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_3_4 * -------------------------------- #
class C6_3_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_3_4
        labels = dc6_3_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_3_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_3_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_3_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_3_4


# Update Form
class C6_3_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_3_4
        labels = dc6_3_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_3_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_3_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_3_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_3_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_3_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_3_5 * -------------------------------- #
class C6_3_5CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_3_5
        labels = dc6_3_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_3_5')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_3_5'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_3_5CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_3_5


# Update Form
class C6_3_5UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_3_5
        labels = dc6_3_5
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_3_5UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_3_5UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_3_5SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_3_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_3_5SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_4_1 * -------------------------------- #
class C6_4_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_4_1
        labels = dc6_4_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_4_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_4_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_4_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_4_1


# Update Form
class C6_4_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_4_1
        labels = dc6_4_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_4_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_4_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_4_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_4_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_4_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_4_2 * -------------------------------- #
class C6_4_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_4_2
        labels = dc6_4_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_4_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_4_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_4_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_4_2


# Update Form
class C6_4_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_4_2
        labels = dc6_4_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_4_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_4_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_4_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_4_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_4_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_4_3 * -------------------------------- #
class C6_4_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_4_3
        labels = dc6_4_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_4_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_4_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_4_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_4_3


# Update Form
class C6_4_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_4_3
        labels = dc6_4_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_4_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_4_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_4_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_4_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_4_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_5_1 * -------------------------------- #
class C6_5_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_5_1
        labels = dc6_5_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_5_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_5_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_5_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_5_1


# Update Form
class C6_5_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_5_1
        labels = dc6_5_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_5_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_5_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_5_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_5_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_5_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_5_2 * -------------------------------- #
class C6_5_2CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_5_2
        labels = dc6_5_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_5_2')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_5_2'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_5_2CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_5_2


# Update Form
class C6_5_2UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_5_2
        labels = dc6_5_2
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_5_2UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_5_2UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_5_2SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_5_2
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_5_2SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_5_3 * -------------------------------- #
class C6_5_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_5_3
        labels = dc6_5_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_5_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_5_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_5_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_5_3


# Update Form
class C6_5_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_5_3
        labels = dc6_5_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_5_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_5_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_5_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_5_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_5_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_5_4 * -------------------------------- #
class C6_5_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_5_4
        labels = dc6_5_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_5_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_5_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_5_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_5_4


# Update Form
class C6_5_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_5_4
        labels = dc6_5_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_5_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_5_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_5_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_5_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_5_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 6_5_5 * -------------------------------- #
class C6_5_5CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_5_5
        labels = dc6_5_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c6_5_5')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c6_5_5'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C6_5_5CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc6_5_5


# Update Form
class C6_5_5UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc6_5_5
        labels = dc6_5_5
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C6_5_5UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C6_5_5UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C6_5_5SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc6_5_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C6_5_5SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_1 * -------------------------------- #
class C7_1_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_1
        labels = dc7_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_1


# Update Form
class C7_1_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_1
        labels = dc7_1_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_2A * -------------------------------- #
class C7_1_2ACreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_2A
        labels = dc7_1_2A
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_2A')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_2A'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_2ACreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_2A


# Update Form
class C7_1_2AUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_2A
        labels = dc7_1_2A
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_2AUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_2AUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_2ASearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_2A
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_2ASearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_2B * -------------------------------- #
class C7_1_2BCreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_2B
        labels = dc7_1_2B
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_2B')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_2B'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_2BCreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_2B


# Update Form
class C7_1_2BUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_2B
        labels = dc7_1_2B
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_2BUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_2BUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_2BSearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_2B
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_2BSearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_2C * -------------------------------- #
class C7_1_2CCreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_2C
        labels = dc7_1_2C
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_2C')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_2C'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_2CCreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_2C


# Update Form
class C7_1_2CUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_2C
        labels = dc7_1_2C
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_2CUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_2CUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_2CSearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_2C
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_2CSearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_3 * -------------------------------- #
class C7_1_3CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_3
        labels = dc7_1_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_3')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_3'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_3CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_3


# Update Form
class C7_1_3UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_3
        labels = dc7_1_3
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_3UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_3UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_3SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_3
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_3SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_4 * -------------------------------- #
class C7_1_4CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_4
        labels = dc7_1_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_4')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_4'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_4CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_4


# Update Form
class C7_1_4UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_4
        labels = dc7_1_4
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_4UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_4UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_4SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_4
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_4SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_5 * -------------------------------- #
class C7_1_5CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_5
        labels = dc7_1_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_5')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_5'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_5CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_5


# Update Form
class C7_1_5UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_5
        labels = dc7_1_5
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_5UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_5UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_5SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_5
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_5SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_6 * -------------------------------- #
class C7_1_6CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_6
        labels = dc7_1_6
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_6')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_6'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_6CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_6


# Update Form
class C7_1_6UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_6
        labels = dc7_1_6
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_6UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_6UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_6SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_6
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_6SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_7A * -------------------------------- #
class C7_1_7ACreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_7A
        labels = dc7_1_7A
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_7A')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_7A'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_7ACreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_7A


# Update Form
class C7_1_7AUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_7A
        labels = dc7_1_7A
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_7AUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_7AUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_7ASearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_7A
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_7ASearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_7B * -------------------------------- #
class C7_1_7BCreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_7B
        labels = dc7_1_7B
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_7B')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_7B'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_7BCreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_7B


# Update Form
class C7_1_7BUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_7B
        labels = dc7_1_7B
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_7BUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_7BUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_7BSearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_7B
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_7BSearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_7C * -------------------------------- #
class C7_1_7CCreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_7C
        labels = dc7_1_7C
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_7C')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_7C'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_7CCreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_7C


# Update Form
class C7_1_7CUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_7C
        labels = dc7_1_7C
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_7CUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_7CUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_7CSearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_7C
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_7CSearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_7D * -------------------------------- #
class C7_1_7DCreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_7D
        labels = dc7_1_7D
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_7D')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_7D'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_7DCreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_7D


# Update Form
class C7_1_7DUpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_7D
        labels = dc7_1_7D
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_7DUpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_7DUpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_7DSearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_7D
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_7DSearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_8 * -------------------------------- #
class C7_1_8CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_8
        labels = dc7_1_8
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_8')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_8'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_8CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_8


# Update Form
class C7_1_8UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_8
        labels = dc7_1_8
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_8UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_8UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_8SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_8
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_8SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_9 * -------------------------------- #
class C7_1_9CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_9
        labels = dc7_1_9
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_9')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_9'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_9CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_9


# Update Form
class C7_1_9UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_9
        labels = dc7_1_9
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_9UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_9UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_9SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_9
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_9SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_10 * -------------------------------- #
class C7_1_10CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_10
        labels = dc7_1_10
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_10')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_10'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_10CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_10


# Update Form
class C7_1_10UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_10
        labels = dc7_1_10
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_10UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_10UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_10SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_10
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_10SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_11 * -------------------------------- #
class C7_1_11CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_11
        labels = dc7_1_11
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_11')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_11'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_11CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_11


# Update Form
class C7_1_11UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_11
        labels = dc7_1_11
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_11UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_11UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_11SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_11
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_11SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_12 * -------------------------------- #
class C7_1_12CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_12
        labels = dc7_1_12
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_12')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_12'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_12CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_12


# Update Form
class C7_1_12UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_12
        labels = dc7_1_12
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_12UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_12UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_12SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_12
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_12SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_13 * -------------------------------- #
class C7_1_13CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_13
        labels = dc7_1_13
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_13')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_13'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_13CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_13


# Update Form
class C7_1_13UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_13
        labels = dc7_1_13
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_13UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_13UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_13SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_13
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_13SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_14 * -------------------------------- #
class C7_1_14CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_14
        labels = dc7_1_14
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_14')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_14'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_14CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_14


# Update Form
class C7_1_14UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_14
        labels = dc7_1_14
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_14UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_14UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_14SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_14
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_14SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_15 * -------------------------------- #
class C7_1_15CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_15
        labels = dc7_1_15
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_15')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_15'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_15CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_15


# Update Form
class C7_1_15UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_15
        labels = dc7_1_15
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_15UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_15UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_15SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_15
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_15SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_16 * -------------------------------- #
class C7_1_16CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_16
        labels = dc7_1_16
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_16')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_16'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_16CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_16


# Update Form
class C7_1_16UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_16
        labels = dc7_1_16
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_16UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_16UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_16SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_16
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_16SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_17 * -------------------------------- #
class C7_1_17CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_17
        labels = dc7_1_17
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_17')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_17'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_17CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_17


# Update Form
class C7_1_17UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_17
        labels = dc7_1_17
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_17UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_17UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_17SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_17
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_17SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_18 * -------------------------------- #
class C7_1_18CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_18
        labels = dc7_1_18
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_18')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_18'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_18CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_18


# Update Form
class C7_1_18UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_18
        labels = dc7_1_18
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_18UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_18UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_18SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_18
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_18SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_1_19 * -------------------------------- #
class C7_1_19CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_19
        labels = dc7_1_19
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_1_19')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_1_19'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_1_19CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_1_19


# Update Form
class C7_1_19UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_1_19
        labels = dc7_1_19
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_1_19UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_1_19UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_1_19SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_1_19
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_1_19SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_2_1 * -------------------------------- #
class C7_2_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_2_1
        labels = dc7_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_2_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_2_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_2_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_2_1


# Update Form
class C7_2_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_2_1
        labels = dc7_2_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_2_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_2_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_2_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_2_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_2_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False


# ------------------------* Forms for Criteria 7_3_1 * -------------------------------- #
class C7_3_1CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_3_1
        labels = dc7_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c7_3_1')
        except:
            cid = None
        initial = kwargs.get('initial', {})
        initial['criterion'] = 'c7_3_1'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C7_3_1CreateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)
            self.fields['paper'].queryset = Subject.objects.none()
            if 'program' in self.data:
                try:
                    program_id = int(self.data.get('program'))
                    self.fields['paper'].queryset = Subject.objects.filter(program_id=program_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['paper'].queryset = self.instance.program.subject_set.order_by('name')

    def field_data(self, *args, **kwargs):
        field_tuple = fc7_3_1


# Update Form
class C7_3_1UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc7_3_1
        labels = dc7_3_1
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C7_3_1UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C7_3_1UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C7_3_1SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc7_3_1
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C7_3_1SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False

