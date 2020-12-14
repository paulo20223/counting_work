from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.template.loader import render_to_string
from django.urls import reverse
from weasyprint import HTML

from apps.company.models import Company
from apps.invoice.form import InvoiceForm
from apps.invoice.models import Invoice
from core.views import AbsView


class InvoiceView(AbsView):
    template_name = 'invoice/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['invoices'] = self.get_paginator(Invoice.objects.all().order_by('-date_creation'))
        return context

    def post(self, request, **kwargs):
        form = InvoiceForm(data=request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('invoice:list'))


class InvoiceDetailView(AbsView):
    template_name = 'invoice/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['invoice'] = get_object_or_404(Invoice, pk=kwargs.get("key"))
        context['all_companies'] = Company.objects.all()
        return context

    def post(self, request, **kwargs):
        obj = get_object_or_404(Invoice, pk=kwargs.get("id"))
        form = InvoiceForm(instance=obj, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('invoice:detail', kwargs=kwargs))


class InvoiceFileView(AbsView):

    def get(self, request, **kwargs):
        context = {'invoice': get_object_or_404(Invoice, pk=kwargs.get("key")),
                   'all_companies': Company.objects.all()}
        html = HTML(string=render_to_string('invoice/pdf.html', context=context, request=request))
        main_doc = html.render()
        pdf = main_doc.write_pdf()
        return HttpResponse(pdf, content_type='application/pdf')
