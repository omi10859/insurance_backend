from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils import proccess_file


class ImportCSV(APIView):

    def post(self, *args, **kwargs):
        
        file = self.request.FILES.get('csv_file', False)   
        
        if not file:
            return Response('Error File not Found', status=status.HTTP_400_BAD_REQUEST)

        proccess_file(file)

        return Response('File Added Successfully')
