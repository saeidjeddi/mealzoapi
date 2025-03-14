from rest_framework import serializers
from .models import Foodhouse



class FoodhouseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Foodhouse
        fields = '__all__'

