from rest_framework import serializers
from .models import ScoffableList



class ScoffableSerializers(serializers.ModelSerializer):
    class Meta:
        model = ScoffableList
        fields = '__all__'