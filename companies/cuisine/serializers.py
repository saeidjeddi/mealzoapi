from rest_framework import serializers
from .models import CuisineCategory


class CuisineSerializers(serializers.ModelSerializer):
    class Meta:
        model = CuisineCategory
        fields = '__all__'