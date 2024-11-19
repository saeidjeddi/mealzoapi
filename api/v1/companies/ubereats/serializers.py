from rest_framework import serializers
from .models import UberEats



class UberEatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = UberEats
        fields = '__all__'
