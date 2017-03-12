from animals.models import Kitten, Puppy
from rest_framework import serializers


class KittenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitten
        fields = '__all__'


class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        fields = '__all__'
