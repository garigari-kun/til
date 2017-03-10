from animals.models import Kitten
from rest_framework import serializers


class KittenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitten
