from rest_framework import serializers
from .models import Justeat


class JusteatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Justeat
        fields = '__all__'