from django.urls import path

from apps.company.views import CompanyView, CompanyDetailView

app_name = 'company'

urlpatterns = [
    path('', CompanyView.as_view(), name="list"),
    path('<int:id>/', CompanyDetailView.as_view(), name="detail"),

]
