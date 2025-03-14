from rest_framework.generics import ListAPIView
from .models import Justeat
from .serializers import JusteatSerializers
from rest_framework.permissions import IsAuthenticated
import time
from permissions.userAuth import Member


class JusteatApiView(ListAPIView):
    queryset = Justeat.objects.all()
    serializer_class = JusteatSerializers
    permission_classes = [Member]