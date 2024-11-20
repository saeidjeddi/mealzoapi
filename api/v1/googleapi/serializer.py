from rest_framework import serializers



class TimePeriodSerializer(serializers.Serializer):
    openDay = serializers.CharField()
    openTime = serializers.DictField(child=serializers.IntegerField())
    closeDay = serializers.CharField()
    closeTime = serializers.DictField(child=serializers.IntegerField())


class RegularHoursSerializer(serializers.Serializer):
    periods = TimePeriodSerializer(many=True)


class UpdateTitleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)


class UpdatePhoneNumbersSerializer(serializers.Serializer):
    primaryPhone = serializers.CharField(max_length=255, required=True)

class UpdatePhoneNumbers(serializers.Serializer):
    phoneNumbers = UpdatePhoneNumbersSerializer()


class UpdateWebsiteUriSerializer(serializers.Serializer):
    websiteUri = serializers.CharField(max_length=255, required=True)