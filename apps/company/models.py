from django.db import models

from core.models import AbsModel


class Company(AbsModel):
    name = models.CharField("Название компании", max_length=1000)
    address = models.CharField("Адресс", max_length=1000)
    unn = models.CharField("Индефикационный код", max_length=1000)

    def __str__(self):
        return f'{self.name}'
