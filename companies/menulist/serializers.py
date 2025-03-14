from rest_framework import serializers
from .models import MenuList

class MenuListSerializers(serializers.ModelSerializer):
    class Meta:
        model = MenuList
        fields = '__all__'