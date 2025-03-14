from rest_framework.generics import ListAPIView
from .models import PostCodes
from .serializers import PostcodeSerializers




class PostcodeApiView(ListAPIView):
    queryset = PostCodes.objects.all()
    serializer_class = PostcodeSerializers
