from django.shortcuts import get_object_or_404
from rest_framework import serializers

from ads.models.ad import Ad
from ads.models.category import Category
from ads.serializers.category import CategorySerializer
from users.models import User
from users.serializer import UserSerializer


class AdSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Ad
        fields = "__all__"


class AdCreateSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=User.objects.all(),
        slug_field='name'
    )

    category = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    def is_valid(self, raise_exception=False):
        self._author = self.initial_data.pop('author', None)
        self._category = self.initial_data.pop('category', None)
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        ad = Ad.objects.create(**validated_data)

        if self._author:
            for author in self._author:
                obj, _ = User.objects.get(name=author)
                ad.author.add(obj)

        if self._category:
            for category in self._category:
                obj, _ = Category.objects.get_or_create(name=category)
                ad.author.add(obj)

        return ad

    class Meta:
        model = Ad
        fields = '__all__'


class AdUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    image = serializers.ImageField(required=False)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Ad
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._category_id = self.initial_data.pop('category_id')
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        ad = super().save()
        ad.category = get_object_or_404(Category, pk=self._category_id)
        ad.save()

        return ad


class AdImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    is_published = serializers.BooleanField(read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'

