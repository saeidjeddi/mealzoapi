from rest_framework import serializers
from .models import Deliveroo


class DeliverooSerializers(serializers.ModelSerializer):
    class Meta:
        model = Deliveroo
        fields = '__all__'
        #exclude = ('cuisines', 'total_reviews', 'rating')