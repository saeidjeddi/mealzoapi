from rest_framework.generics import ListAPIView
from .models import Kuick
from .serializers import KuickSerializers
from rest_framework.permissions import IsAuthenticated
from permissions.userAuth import Member

class KuickApiView(ListAPIView):
    queryset = Kuick.objects.all()
    serializer_class = KuickSerializers
    permission_classes = [Member]