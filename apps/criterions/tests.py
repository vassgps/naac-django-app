from django.test import TestCase

# Create your tests here.

# Copied Temp data from  field names

""" 
#For importing to AutoUpdate.generator.create for Automatically Generate HTML files based on Fields in this dict.

all_field_keys = {"c1_1_1": fc1_1_1[:-2], "c1_1_2": fc1_1_2[:-2]}

#For importing to Criterions.criterion for Automatically Generate HTML Table Headers based on Fields in this dict.

all_field_values = {"c1_1_1": dc1_1_1, "c1_1_2": dc1_1_2}
"""

"""
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

"""