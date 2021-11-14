
# ------------------------* Forms for Criteria 2.1.1 * -------------------------------- #
from django import forms
from naac.apps.adminapp.models import FinalCriteria
from naac.apps.criterions.fields.field_names import fc1_1_1, dc1_1_1
from naac.apps.criterions.forms import widget_dict
from naac.apps.criterions.models import CriterionMaster
from naac.apps.programs.models import Program, Subject


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



# ------------------------* Forms for Criteria 2.1.2 * -------------------------------- #
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



# ------------------------* Forms for Criteria 2.1.3 * -------------------------------- #
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



# ------------------------* Forms for Criteria 2.2.1 * -------------------------------- #
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



# ------------------------* Forms for Criteria 2.2.2 * -------------------------------- #
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



# ------------------------* Forms for Criteria 2.2.3 * -------------------------------- #
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



# ------------------------* Forms for Criteria 2.3.1 * -------------------------------- #
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



# ------------------------* Forms for Criteria 2.3.2 * -------------------------------- #
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


# ------------------------* Forms for Criteria 2.3.3 * -------------------------------- #
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


# ------------------------* Forms for Criteria 2.3.4 * -------------------------------- #
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


# ------------------------* Forms for Criteria 2.4.1 * -------------------------------- #
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


# ------------------------* Forms for Criteria 2.4.2 * -------------------------------- #
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


# ------------------------* Forms for Criteria 2.4.3 * -------------------------------- #
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



# ------------------------* Forms for Criteria 2.4.4 * -------------------------------- #
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



# ------------------------* Forms for Criteria 2.4.5 * -------------------------------- #
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



# ------------------------* Forms for Criteria 2.5.1 * -------------------------------- #
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



# ------------------------* Forms for Criteria 2.5.2 * -------------------------------- #
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



# ------------------------* Forms for Criteria 2.5.3 * -------------------------------- #
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



# ------------------------* Forms for Criteria 2.5.4 * -------------------------------- #
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



# ------------------------* Forms for Criteria 2.5.5 * -------------------------------- #
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



# ------------------------* Forms for Criteria 2.6.1 * -------------------------------- #
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



# ------------------------* Forms for Criteria 2.6.2 * -------------------------------- #
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



# ------------------------* Forms for Criteria 2.6.3 * -------------------------------- #
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


# ------------------------* Forms for Criteria 2.7.1 * -------------------------------- #
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



# ------------------------* Forms for Criteria 3.1.1 * -------------------------------- #
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
