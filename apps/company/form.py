from django import forms

from apps.company.models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'address', 'unn')
