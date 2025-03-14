from rest_framework.generics import ListAPIView
from .models import WhatTheFork
from .serializers import  WsSerializers
from rest_framework.permissions import IsAuthenticated
from permissions.userAuth import Member

class WsApiView(ListAPIView):
    queryset = WhatTheFork.objects.all()
    permission_classes = [Member]
    serializer_class = WsSerializers