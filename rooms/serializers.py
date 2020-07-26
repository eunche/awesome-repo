from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Room


class RoomSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Room
        fields = ("pk", "name", "price", "user")


class BigRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ()
