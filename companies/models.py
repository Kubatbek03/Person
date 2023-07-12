from django.db import models
from users.models import User


class Company(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    logo = models.ImageField(upload_to='company_logo')
    address = models.CharField(max_length=150)
    finance = models.IntegerField(default=0)
    personals = models.ManyToManyField(User, related_name='company_personals')

    def __str__(self):
        return self.name


