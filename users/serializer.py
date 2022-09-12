from rest_framework import serializers

from ads.models.location import Location
from ads.serializers.location import LocationSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    location = LocationSerializer(read_only=True)

    class Meta:
        model = User
        fields = "__all__"


class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop('locations', None)
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        if self._locations:
            for locations in self._locations:
                location_obj, _ = Location.objects.get_or_create(name=locations)
                user.location.add(location_obj)

        return user

    class Meta:
        model = User
        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)

    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop('location')
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        location, _ = Location.objects.get_or_create(name=self._location)
        user.location = location
        user.save()

        return user
