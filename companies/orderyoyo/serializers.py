from rest_framework import serializers
from .models import Orderyoyo



class OrderyoyoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orderyoyo
        fields = '__all__'