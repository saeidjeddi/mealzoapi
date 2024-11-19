from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Foodhub
from .serializers import FoothubSerializers




class FoothubApiView(ListAPIView):
    queryset = Foodhub.objects.all()
    serializer_class = FoothubSerializers
    permission_classes = [IsAuthenticated]


