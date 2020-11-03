from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from apps.company.form import CompanyForm
from apps.company.models import Company
from core.views import AbsView


class CompanyView(AbsView):
    template_name = 'company/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companys'] = self.get_paginator(Company.objects.all().order_by('-date_creation'))
        return context

    def post(self, request, **kwargs):
        form = CompanyForm(data=request.data)
        if form.is_valid():
            form.save()
        return redirect(reverse('company:list'))


class CompanyDetailView(AbsView):
    template_name = 'company/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = get_object_or_404(Company, pk=kwargs.get("id"))
        return context

    def post(self, request, **kwargs):
        company = get_object_or_404(Company, pk=kwargs.get("id"))
        form = CompanyForm(instance=company, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('company:detail', kwargs=kwargs))
