import csv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from rest_framework.parsers import MultiPartParser


class UploadCSV(APIView):

    def post(self, request):
        csv_file = request.FILES['file']
        
        data = csv_file.read().decode('UTF-8')
        lines = data.split('\n')
        reader = csv.DictReader(lines)
        
        for row in reader:
            serializer = UserSerializer(data=row)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message': 'CSV data uploaded successfully'}, status=status.HTTP_201_CREATED)
    


class RetrieveData(APIView):
    def get(self, request):
        column = request.GET.get('column')
        order = request.GET.get('order')
        if order not in ['asc', 'desc']:
            return Response({'error': 'Invalid parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        ordering = f"{'-' if order == 'desc' else ''}{column}"
        queryset = User.objects.order_by(ordering)[:50]
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    

        
        