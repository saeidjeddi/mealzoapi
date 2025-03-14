from rest_framework.generics import ListAPIView
from .models import ScoffableList
from .serializers import ScoffableSerializers
from rest_framework.permissions import IsAuthenticated
import time
from permissions.userAuth import Member



class ScoffableApiView(ListAPIView):
    queryset = ScoffableList.objects.all()
    serializer_class = ScoffableSerializers
    permission_classes = [Member]