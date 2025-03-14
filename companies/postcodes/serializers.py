from rest_framework import serializers
from .models import PostCodes


class PostcodeSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostCodes
        fields = '__all__'