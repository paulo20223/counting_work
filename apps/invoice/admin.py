from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path

from apps.invoice.models import WorkExample, WorkItem, Invoice


class WorkInline(admin.TabularInline):
    fields = ("name", "hour", "cost_by_hour", "invoice")
    readonly_fields = ("price",)
    model = WorkItem


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = [
        WorkInline,
    ]


@admin.register(WorkItem)
class WorkItemAdmin(admin.ModelAdmin):

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import_works/', self.import_works),
        ]
        return my_urls + urls

    @staticmethod
    def import_works(request):
        return HttpResponseRedirect("../")
