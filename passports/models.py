from django.db import models
from users.models import User


CHOICE_GENDER = (
    ('мужской', 'Мужской'),
    ('женский', 'Женский'),
)

CHOICE_NATION = (
    ('кыргыз', 'Кыргыз'),
    ('орус', 'Орус'),
    ('американец', 'Американец')
)


class Passport(models.Model):
    id_passport = models.CharField(max_length=9, unique=True)
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='passport_image')
    birthday = models.DateField()
    gender = models.CharField(max_length=10, choices=CHOICE_GENDER)
    nation = models.CharField(max_length=15, choices=CHOICE_NATION)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_passport')
    created_at = models.DateField(auto_created=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - owner: {self.owner}"


    

