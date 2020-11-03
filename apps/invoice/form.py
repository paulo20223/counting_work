from django import forms

from apps.invoice.models import Invoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('key', 'issue_date', 'due_date', 'company_from', 'company_to')
