from rest_framework.generics import ListAPIView
from .models import WhatTheFork
from .serializers import  WsSerializers
from rest_framework.permissions import IsAuthenticated


class WsApiView(ListAPIView):
    queryset = WhatTheFork.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = WsSerializers



