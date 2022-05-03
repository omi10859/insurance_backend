from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserPolicy
from .serializers import UserPolicySerializer, UserPolicyUpdateSerializer
from .utils import get_chart_data

class UserPolicyListView(generics.ListAPIView):

    queryset = UserPolicy.objects.all()
    serializer_class = UserPolicySerializer

    search_fields = ['policy_id', 'customer_id', ]
    filter_backends = (filters.SearchFilter, )

class UserPolicyView(generics.RetrieveUpdateAPIView):

    queryset = UserPolicy.objects.all()

    def get_serializer_class(self):

        if self.request.method == 'PUT':
            return UserPolicyUpdateSerializer

        return UserPolicySerializer

class UserPolicyChartView(APIView):

    def get(self, *args, **kwargs):
        data = get_chart_data()
        
        return Response(data)

