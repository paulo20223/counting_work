from django.urls import path

from apps.invoice.views import InvoiceView

app_name = 'invoice'

urlpatterns = [
    path('', InvoiceView.as_view(), name="list"),
]
