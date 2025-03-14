from rest_framework import serializers
from .models import City, Region


class CitySerializers(serializers.ModelSerializer):
        class Meta:
            model = City
            fields = '__all__'


class RegionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'