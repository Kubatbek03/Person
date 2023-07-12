from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=150)
    capital = models.CharField(max_length=150)
    flag = models.ImageField(upload_to='country_flag')
    hymn = models.FileField(upload_to='country_hymn')
    population = models.IntegerField(default=0)
    total_area = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=150)
    index = models.CharField(max_length=50)
    region = models.CharField(max_length=150)
    population = models.IntegerField(default=0)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='country_city')

    def __str__(self):
        return f"{self.name} - {self.country}"
