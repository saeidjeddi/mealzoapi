# from rest_framework.generics import ListAPIView
from .models import Foodhub
from .serializers import FoodhubSerializers
from permissions.userAuth import Member
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.timezone import now
from accounts.models import User





class FoodhubApiView(APIView):
    # permission_classes = [Member]

    def get(self, request):
        if request.user.isLimited:
            if request.user.numberOfRequestRemaining > 0:
                request.user.numberOfRequestRemaining -= 1
                request.user.save()
                queryset = Foodhub.objects.all()
                serialized_data = FoodhubSerializers(queryset, many=True).data
                return Response(serialized_data)
            else:
                return Response({'message': 'Request limit reached'}, status=403)
        else:
            queryset = Foodhub.objects.all()
            serialized_data = FoodhubSerializers(queryset, many=True).data
            return Response(serialized_data)


# class FoodhubApiView(ListAPIView):
#     queryset = Foodhub.objects.all()
#     serializer_class = FoodhubSerializers
#     permission_classes = [Member]

    # def get_serializer(self, *args, **kwargs):
    #     fields = self.request.query_params.get('fields')
    #     if fields:
    #         fields = fields.split(',')
    #         kwargs['fields'] = fields
    #     return super().get_serializer(*args, **kwargs)