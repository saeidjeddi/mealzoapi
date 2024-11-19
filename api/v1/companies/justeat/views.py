from rest_framework.generics import ListAPIView
from .models import Justeat
from .serializers import JusteatSerializers
from rest_framework.permissions import IsAuthenticated


class JusteatApiView(ListAPIView):
    queryset = Justeat.objects.all()
    serializer_class = JusteatSerializers
    # permission_classes = [IsAuthenticated]



