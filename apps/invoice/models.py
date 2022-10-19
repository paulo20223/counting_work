from django.db import models
from django.db.models import Sum, F

from apps.company.models import Company
from core.models import AbsModel
from core.settings import TWO_PLACES


class Invoice(AbsModel):
    key = models.IntegerField("Индефикационный код", primary_key=True)
    issue_date = models.DateField("Дата создания")
    due_date = models.DateField("Дата выставления")
    base_cost_by_hour = models.DecimalField("Базовая цена за час", decimal_places=2, max_digits=100)
    company_from = models.ForeignKey(Company, on_delete=models.SET_NULL, related_name="invoice_from",
                                     null=True, blank=True)
    company_to = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, related_name="invoice_to")

    def total(self):
        return self.items.aggregate(total=Sum(F('hour') * F('cost_by_hour')))['total'].quantize(TWO_PLACES)

    def total_hours(self):
        return self.items.aggregate(total_hours=Sum(F('hour')))['total_hours']

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
    cost_by_hour = models.DecimalField("Цена за час", decimal_places=2, max_digits=100, blank=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.SET_NULL, null=True, blank=True, related_name="items")

    @property
    def price(self):
        return (self.hour * self.cost_by_hour).quantize(TWO_PLACES)

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return f'{self.name}'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.cost_by_hour:
            self.cost_by_hour = self.invoice.base_cost_by_hour
        super().save(force_insert, force_update, using, update_fields)
