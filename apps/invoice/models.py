from django.db import models

from apps.company.models import Company
from core.models import AbsModel


class Invoice(AbsModel):
    key = models.IntegerField("Индефикационный код", primary_key=True)
    issue_date = models.DateField("Дата создания")
    due_date = models.DateField("Дата выставления")
    company_from = models.ForeignKey(Company, on_delete=models.SET_NULL, related_name="invoice_from",
                                     null=True, blank=True)
    company_to = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, related_name="invoice_to")

    class Meta:
        verbose_name = 'Счет фактура'
        verbose_name_plural = 'Счет фактуры'

    def __str__(self):
        return f'{self.key} {self.issue_date}'


class WorkExample(AbsModel):
    name = models.CharField("Название работы", max_length=1000)

    class Meta:
        verbose_name = 'Шаблон работы'
        verbose_name_plural = 'Шаблоны работ'

    def __str__(self):
        return f'{self.name}'


class WorkItem(AbsModel):
    name = models.CharField("Название работы", max_length=1000)
    hour = models.DecimalField("Количество часов", decimal_places=2, max_digits=100)
    cost_by_hour = models.DecimalField("Цена за час", decimal_places=2, max_digits=100)
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return f'{self.name}'
