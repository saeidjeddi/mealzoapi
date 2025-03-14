from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import CuisineCategory
from .serializers import CuisineSerializers




class CuisineApiView(ListAPIView):
    queryset = CuisineCategory.objects.all()
    serializer_class = CuisineSerializers
