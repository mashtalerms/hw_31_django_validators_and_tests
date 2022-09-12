from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from ads.models.category import Category
from users.models import User


def check_if_not_published(value):
    if value == True:
        raise ValidationError("Значение поля is_published при создании объявления не может быть True.")


class Ad(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, null=False, blank=False, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=1000, null=True, blank=True)
    is_published = models.BooleanField(default=False, validators=[check_if_not_published])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="images/", null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ["id"]

    def __str__(self):
        return self.name
