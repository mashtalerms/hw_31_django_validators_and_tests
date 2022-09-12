from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, MinValueValidator
from django.db import models

from ads.models.location import Location
from users.validators import check_if_user_older_9, check_if_not_rambler


class User(AbstractUser):

    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLE = [(MEMBER, MEMBER), (MODERATOR, MODERATOR), (ADMIN, ADMIN)]

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(choices=ROLE, max_length=9, default=MEMBER)
    age = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MinValueValidator])
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    birth_date = models.DateField(null=True, validators=[check_if_user_older_9])
    email = models.EmailField(null=True, blank=True, unique=True, validators=[EmailValidator, check_if_not_rambler])

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['username']

    def __str__(self):
        return self.username
