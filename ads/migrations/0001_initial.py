# Generated by Django 4.1 on 2022-09-09 11:30

import ads.models.ad
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ad",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "name",
                    models.CharField(
                        max_length=300,
                        validators=[django.core.validators.MinLengthValidator(10)],
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                (
                    "description",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=False, validators=[ads.models.ad.check_if_not_published]
                    ),
                ),
                ("image", models.ImageField(null=True, upload_to="images/")),
            ],
            options={
                "verbose_name": "Объявление",
                "verbose_name_plural": "Объявления",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                (
                    "slug",
                    models.SlugField(
                        max_length=10,
                        null=True,
                        unique=True,
                        validators=[django.core.validators.MinLengthValidator(5)],
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("lat", models.CharField(max_length=30)),
                ("lng", models.CharField(max_length=30)),
            ],
            options={
                "verbose_name": "Локация",
                "verbose_name_plural": "Локации",
            },
        ),
        migrations.CreateModel(
            name="Selection",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("items", models.ManyToManyField(to="ads.ad")),
            ],
            options={
                "verbose_name": "Подборка",
                "verbose_name_plural": "Подборки",
            },
        ),
    ]
