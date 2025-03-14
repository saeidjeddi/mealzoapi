from rest_framework.generics import ListAPIView
from .models import Foodhouse
from .serializers import FoodhouseSerializers
from rest_framework.permissions import IsAuthenticated
from permissions.userAuth import Member



class FoodhouseApiView(ListAPIView):
    queryset = Foodhouse.objects.all()
    serializer_class = FoodhouseSerializers
    permission_classes = [Member]

