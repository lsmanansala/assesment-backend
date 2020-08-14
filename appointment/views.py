from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import AppointmentSerializer
from .models import Appointment
from rest_framework.response import Response
from django.db.models.query import Q


class AppointmentView(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


    def create(self, request):
        """
        Create View Function for creating Appointments
        """
        data = request.data
        serializer = AppointmentSerializer(data=data)
           
        if serializer.is_valid():
            saved = serializer.save()

            if(saved['success'] == True):
                return Response(data, status = status.HTTP_200_OK)
            return Response({'error':saved['message']}, status=status.HTTP_200_OK)
        
        return Response({'error': "unable to create appointment"}, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Function for retrieving single appointment using PK
        """
        try:
            appointment = Appointment.objects.get(pk=pk)
            serializer = AppointmentSerializer(appointment)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'error': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
    
