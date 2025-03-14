from rest_framework import serializers
from .models import WhatTheFork



class WsSerializers(serializers.ModelSerializer):
    class Meta:
        model = WhatTheFork
        fields = '__all__'