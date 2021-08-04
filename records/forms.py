from records.models import Person
from django.forms import ModelForm
from django import forms


class PersonForm(forms.ModelForm):
    update_plans = forms.BooleanField(required=False)

    class Meta:
        model = Person
        fields = '__all__'


# class PlanForm(ModelForm):
#     class Meta:
#         model = Plan
#         exclude = ['profile']
