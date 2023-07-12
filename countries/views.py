from django.shortcuts import render, redirect
from countries.models import Country


def get_countries(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        return render(request, 'countries/index.html', {'countries': countries})


def get_country(request, id):
    if request.method == 'GET':
        country = Country.objects.get(id=id)
        return render(request, 'countries/detail.html', {'country': country})


def post_country(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        capital = request.POST.get('capital')
        flag = request.FILES.get('flag')
        hymn = request.FILES.get('hymn')
        population = request.POST.get('population')
        total_area = request.POST.get('total_area')
        post_obj = Country.objects.create(name=name, capital=capital, flag=flag, hymn=hymn, population=population, total_area=total_area)
    return render(request, 'countries/create.html')


def update_country(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        capital = request.POST.get('capital')
        flag = request.FILES.get('flag')
        hymn = request.FILES.get('hymn')
        population = request.POST.get('population')
        total_area = request.POST.get('total_area')

        country_obj = Country.objects.get(id=id)
        country_obj.name = name
        country_obj.capital = capital
        country_obj.flag = flag
        country_obj.hymn = hymn
        country_obj.population = population
        country_obj.total_area = total_area
        country_obj.save()
        return redirect('get-country', country_obj.id)
    return render(request, 'countries/update.html')


def country_delete(request, id):
    if request.method == 'POST':
        country_obj = Country.objects.get(id=id)
        country_obj.delete()
        return redirect('list-country')
    return render(request, 'countries/delete.html')