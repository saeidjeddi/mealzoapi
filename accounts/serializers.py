from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import requests
from datetime import datetime
from .models import User


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("The old password is incorrect.", status.HTTP_400_BAD_REQUEST)
        return value

    def validate_new_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("The password must be at least 8 characters.", status.HTTP_400_BAD_REQUEST)

        if value.isdigit():
            raise serializers.ValidationError("The password should not be just numbers.", status.HTTP_400_BAD_REQUEST)

        if value.isalpha():
            raise serializers.ValidationError("The password should not be just characters.", status.HTTP_400_BAD_REQUEST)

        if value.isupper():
            raise serializers.ValidationError("The password should not be just uppercase.", status.HTTP_400_BAD_REQUEST)

        if value.isspace():
            raise serializers.ValidationError("The password should not be just spaces.", status.HTTP_400_BAD_REQUEST)

        if value.islower():
            raise serializers.ValidationError("The password should not be just lowercase.", status.HTTP_400_BAD_REQUEST)

        try:
            validate_password(value, self.context['request'].user)
        except ValidationError as e:
            raise serializers.ValidationError(list(e.messages))

        return value

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "The passwords do not match."}, code=status.HTTP_400_BAD_REQUEST)
        return data

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user



class UpdateRequestRemainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['numberOfRequestRemaining']


class TokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['department'] = user.department,
        token['active'] = user.active,
        token['admin'] = user.admin,
        token['superuser'] = user.superuser,
        token['googleBusinessMap'] = user.googleBusinessMap,
        token['devices'] = user.devices,
        token['companies'] = user.companies,
        token['gbDashboardEdit'] = user.gbDashboardEdit,



        #------------------------------------------------------
        expiration_time = datetime.fromtimestamp(token['exp']).strftime('%Y-%m-%d %H:%M:%S')


        access = {

            'superuser' : user.superuser,
            'googleBusinessMap' : user.googleBusinessMap,
            'gbDashboardEdit' : user.gbDashboardEdit,
            'devices' : user.devices,
            'companies' : user.companies,

        }

        access_department = [key for key, value in access.items() if value]

        access = ' , '.join(access_department)

        message = (
            f"🪪 User_Id : {user.id} \n"
            f"👤 UserName : {user.username} \n"
            f"✉️ Email : {user.email} \n"
            f"----------------- \n"
            f"🔑 Access : {access} \n"
            f" ------------- \n"
            f"⏳ Time : {datetime.now().strftime('%Y-%m-%d %H:%M')} \n"
            f"⌛ Expiration Time : {expiration_time}"
        )

        token_id = "8157771064:AAF_qVGJaGFB__FGn5oruvmfFGVCIlR8kRU"
        my_id = "-1002283091172"


        url = f"https://api.telegram.org/bot{token_id}/sendMessage?chat_id={my_id}&text={message}"
        requests.get(url)
        # ------------------------------------------------------

        return token
