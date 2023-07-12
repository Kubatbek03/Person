from django.shortcuts import render
from companies.models import Company


def list_companies(request):
    companies = Company.objects.all()
    print(companies)
    return render(request, 'companies/index.html', {'companies': companies})


def get_company(request, id):
    company = Company.objects.get(id=id)
    return render(request, 'companies/detail.html', {'company': company})

