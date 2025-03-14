from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import MenuList
from .serializers import MenuListSerializers
import time
from permissions.userAuth import Member



class MenuListApiView(ListAPIView):
    queryset = MenuList.objects.all()
    #time.sleep(300)
    serializer_class = MenuListSerializers
    permission_classes = [Member]