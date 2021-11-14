# Generate Reports.py

all_criterion = ["3_1_1", "3_1_2", "3_1_3", "3_1_4", "3_2_1", "3_2_2",
                 "3_2_3", "3_2_4", "3_3_1", "3_3_2", "3_3_3", "3_4_1", "3_4_2", "3_4_3", "3_4_4", "3_4_5",
                 "3_4_6", "3_4_7", "3_4_8", "3_5_1", "3_5_2", "3_5_3", "3_6_1", "3_6_2", "3_6_3", "3_6_4",
                 "3_7_1", "3_7_2", "3_7_3", "4_1_1", "4_1_2", "4_1_2A", "4_1_2B", "4_1_2C", "4_1_2D",
                 "4_1_2E",
                 "4_1_3", "4_1_4", "4_2_1", "4_2_2", "4_2_3", "4_2_4", "4_2_5", "4_2_6", "4_3_1", "4_3_2",
                 "4_3_3", "4_3_4", "4_4_1", "4_4_2", "5_1_1", "5_1_2", "5_1_3", "5_1_3A", "5_1_3B", "5_1_3C",
                 "5_1_3D", "5_1_3E", "5_1_3F", "5_1_3G", "5_1_3H", "5_1_4", "5_1_5", "5_1_6", "5_2_1",
                 "5_2_2",
                 "5_2_3", "5_3_1", "5_3_2", "5_3_2A", "5_3_2B", "5_3_3", "5_4_1A", "5_4_1B", "5_4_2", "6_1_1",
                 "6_1_2", "6_2_1", "6_2_2", "6_2_3", "6_2_4", "6_3_1", "6_3_2", "6_3_3", "6_3_4", "6_3_5",
                 "6_4_1", "6_4_2", "6_4_3", "6_5_1", "6_5_2", "6_5_3", "6_5_4", "6_5_5", "7_1_1",
                 "7_1_2A", "7_1_2B", "7_1_2C", "7_1_3", "7_1_4", "7_1_5", "7_1_6", "7_1_7A", "7_1_7B",
                 "7_1_7C",
                 "7_1_7D", "7_1_8", "7_1_9", "7_1_10", "7_1_11", "7_1_12", "7_1_13", "7_1_14", "7_1_15",
                 "7_1_16", "7_1_17", "7_1_18", "7_1_19", "7_2_1", "7_3_1"]

for obj_id in all_criterion:
    form_data = f"""
    
# ------------------------* Forms for Criteria {obj_id} * -------------------------------- #
class C{obj_id}CreateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc{obj_id}
        labels = dc{obj_id}
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.field_data(*args, **kwargs)
        try:
            cid = FinalCriteria.objects.get(criteria_id='c{obj_id}')
        except:
            cid = None
        initial = kwargs.get('initial', {{x}})
        initial['criterion'] = 'c{obj_id}'
        initial['final_criteria'] = cid
        kwargs['initial'] = initial
        super(C{obj_id}CreateForm, self).__init__(*args, **kwargs)
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
        field_tuple = fc{obj_id}


# Update Form
class C{obj_id}UpdateForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        # exclude = ('user', 'status', 'is_active', 'criteria_id', 'is_verified',)
        fields = fc{obj_id}
        labels = dc{obj_id}
        widgets = widget_dict

    def save(self, commit=True):
        instance = super(C{obj_id}UpdateForm, self).save(commit=False)
        instance.status = "PENDING"
        if commit:
            instance.save()
        return instance

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(C{obj_id}UpdateForm, self).__init__(*args, **kwargs)
        user_dept = self.user.department.id
        if str(self.user.user_scope) not in ("NAAC_COD", "ADMIN"):
            self.fields['program'].queryset = Program.objects.filter(department=user_dept)


# Search form
class C{obj_id}SearchForm(forms.ModelForm):
    class Meta:
        model = CriterionMaster
        fields = sc{obj_id}
        widgets = widget_dict

    def __init__(self, *args, **kwargs):
        super(C{obj_id}SearchForm, self).__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].required = False

"""
    filename = "form_data.txt"
    fx = open(filename, "a")
    fx.write(form_data)
    fx.close()
print("Success fully Completed..!")
