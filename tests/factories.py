import factory
from faker import Faker

from ads.models.ad import Ad


class AdFactory(factory.django.DjangoModelFactory):
    """Factory for one ad"""
    class Meta:
        model = Ad

    name = "test-factory"
    price = 100


class AdsFactory(factory.django.DjangoModelFactory):
    """Factory for many ads"""
    class Meta:
        model = Ad

    name = Faker().name()
    price = 100
