from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Straightfrom
from .serializers import StraightfromSerializers

from permissions.userAuth import Member


class StraightfromApiView(ListAPIView):
    queryset = Straightfrom.objects.all()
    serializer_class = StraightfromSerializers
    permission_classes = [Member]