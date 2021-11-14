# AdminApp/Utils/Forms.py
from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from ..models import EventUploader, CriteriaManager, FinalCriteria


class MenuCreateForm(forms.ModelForm):
    class Meta:
        model = CriteriaManager
        exclude = ('is_enabled',)
        fields = "__all__"

        # widgets = {
        #     'established_at': DatePickerInput()
        # }


class CriteriaUpdateForm(forms.ModelForm):
    class Meta:
        model = CriteriaManager
        exclude = ('criteria', 'ordering', 'cr_index', 'is_enabled')
        fields = "__all__"


# Add new Program / Cources  or Update
class EventCreateForm(forms.ModelForm):
    class Meta:
        model = EventUploader
        fields = "__all__"
        exclude = ('user', 'status')

        widgets = {
            'date': DatePickerInput(), 'approved_on': DatePickerInput()
        }


class QuestionDataUpdateForm(forms.ModelForm):
    class Meta:
        model = FinalCriteria
        # exclude = ('ordering', 'cr_index', 'majour')
        fields = ('criteria', 'final_title', 'final_description', 'keywords')
