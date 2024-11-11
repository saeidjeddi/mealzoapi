from rest_framework import serializers



class TimePeriodSerializer(serializers.Serializer):
    openDay = serializers.CharField()
    openTime = serializers.DictField(child=serializers.IntegerField())
    closeDay = serializers.CharField()
    closeTime = serializers.DictField(child=serializers.IntegerField())


class RegularHoursSerializer(serializers.Serializer):
    periods = TimePeriodSerializer(many=True)
