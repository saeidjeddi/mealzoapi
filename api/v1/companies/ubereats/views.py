from rest_framework.generics import ListAPIView
from .models import UberEats
from .serializers import UberEatsSerializers
from rest_framework.permissions import IsAuthenticated


class UberEatsApiView(ListAPIView):
    queryset = UberEats.objects.all()
    serializer_class = UberEatsSerializers
    permission_classes = [IsAuthenticated]



