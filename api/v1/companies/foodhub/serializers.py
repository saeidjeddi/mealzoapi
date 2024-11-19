from rest_framework import serializers
from .models import Foodhub


class FoothubSerializers(serializers.ModelSerializer):
        class Meta:
            model = Foodhub
            fields = '__all__'
