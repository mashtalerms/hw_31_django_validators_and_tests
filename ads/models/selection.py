from django.db import models

from ads.models.ad import Ad
from users.models import User


class Selection(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    items = models.ManyToManyField(Ad, null=True, blank=True)

    class Meta:
        verbose_name = "Подборка"
        verbose_name_plural = "Подборки"

    def __str__(self):
        return self.name
