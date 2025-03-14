from rest_framework.generics import ListAPIView
from .models import Orderyoyo
from .serializers import OrderyoyoSerializers
from rest_framework.permissions import IsAuthenticated
import time
from permissions.userAuth import Member

class OrderyoyoApiView(ListAPIView):
    queryset = Orderyoyo.objects.all()

    serializer_class = OrderyoyoSerializers
    permission_classes = [Member]
