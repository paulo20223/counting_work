from django.urls import path

from apps.invoice.views import InvoiceView, InvoiceDetailView, InvoiceFileView

app_name = 'invoice'

urlpatterns = [
    path('', InvoiceView.as_view(), name="list"),
    path('<int:key>/', InvoiceDetailView.as_view(), name="detail"),
    path('<int:key>/pdf/', InvoiceFileView.as_view(), name="pdf"),

]
