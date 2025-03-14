from rest_framework import serializers
from .models import Kuick


class KuickSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kuick
        fields = '__all__'