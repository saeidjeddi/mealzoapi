from rest_framework.generics import ListAPIView
from .models import Deliveroo
from .serializers import DeliverooSerializers
from permissions.userAuth import Member



class DeliverooApiView(ListAPIView):
    queryset = Deliveroo.objects.all()
    serializer_class = DeliverooSerializers
    permission_classes = [Member]