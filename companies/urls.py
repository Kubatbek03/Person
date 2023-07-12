from django.urls import path
from companies.views import list_companies, get_company


urlpatterns = [
    path('', list_companies, name='list-companies'),
    path('company/<int:id>', get_company, name='get-company')
]