from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbsModel(models.Model):
    class Meta:
        abstract = True

    date_creation = models.DateTimeField(verbose_name=_('Date and time created'), auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name=_('Date and time last changed'), auto_now=True)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()


class ErrorLogs(AbsModel):
    type_error = models.CharField("Тип ошибки", max_length=1000)
    message = models.CharField("Тест ошибки", max_length=1000)
    report = models.TextField("Отчёт об ошибке")

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Ошибка системы'
        verbose_name_plural = 'Ошибки системы'


