from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from permissions.userAuth import Member
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils.timezone import now
from .serializers import ChangePasswordSerializer, TokenSerializer , UpdateRequestRemainingSerializer
from datetime import timedelta
from django.shortcuts import get_object_or_404
from .models import User

class UserView(APIView):
    permission_classes = [Member, IsAuthenticated]

    def get(self, request, format=None):
        access = {
            
            'googleBusinessMap' : request.user.googleBusinessMap,
            'gbDashboardMap' : request.user.gbDashboardMap,
            'googleBusinessPanel' : request.user.googleBusinessPanel,
            'gbDashboardEdit' : request.user.gbDashboardEdit,
            'devices' : request.user.devices,
            'companies' : request.user.companies,
        }


        if request.user.isLimited:
            if request.user.timeRequestRemaining < now():
                request.user.numberOfRequestRemaining = request.user.refreshNumberRequest
                request.user.timeRequestRemaining = now() + timedelta(hours=request.user.refreshTimeRequest)
                request.user.save()



        if request.user.isLimited:
            content = {
                'username': request.user.username,
                'email': request.user.email,
                'full_name': request.user.full_name,
                'department': request.user.department,
                'timeRequest': request.user.timeRequestRemaining.strftime("%Y-%m-%d %H:%M"),
                'numberOfRequest': request.user.numberOfRequestRemaining,
                'isLimited' : request.user.isLimited,
                'access': access,
            }
        else:
            content = {
                'username': request.user.username,
                'email': request.user.email,
                'full_name': request.user.full_name,
                'department': request.user.department,
                'isLimited': request.user.isLimited,
                'access': access,
            }



        return Response(content)



class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def put(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateRequestRemainingView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateRequestRemainingSerializer

    def patch(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=request.user.id)
        serializer = UpdateRequestRemainingSerializer(user, data=request.data, partial=True)

        if request.user.timeRequestRemaining < now():

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenView(TokenObtainPairView):
    serializer_class = TokenSerializer