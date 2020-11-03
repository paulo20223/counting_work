from django.shortcuts import redirect
from django.urls import reverse

from apps.invoice.form import InvoiceForm
from apps.invoice.models import Invoice
from core.views import AbsView


class InvoiceView(AbsView):
    template_name = 'invoice.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['invoices'] = self.get_paginator(Invoice.objects.all().order_by('-date_creation'))
        return context

    def post(self, request, **kwargs):
        form = InvoiceForm(data=request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('invoice:list'))
