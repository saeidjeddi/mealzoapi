from rest_framework import serializers
from .models import Straightfrom


class StraightfromSerializers(serializers.ModelSerializer):
    class Meta:
        model = Straightfrom
        fields = '__all__'