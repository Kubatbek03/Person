from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField(default=0)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.id} - {self.first_name} - {self.last_name}"

