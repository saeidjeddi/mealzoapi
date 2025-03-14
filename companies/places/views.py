
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import City
from .serializers import CitySerializers
from .models import City, Region
from .serializers import CitySerializers, RegionSerializers




class CityApiView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializers
    #permission_classes = [IsAuthenticated]



class RegionApiView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializers
    #permission_classes = [IsAuthenticated]