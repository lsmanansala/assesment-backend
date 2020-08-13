from rest_framework import serializers
from .models import Appointment
from rest_framework.response import Response


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'start_date', 'end_date', 'comments', 'completed')


    def create(self, validated_data):
        
        data = validated_data
        appointment = Appointment.objects.create(
            
            patient = data.get('patient'),
            start_date = data.get('start_date'),
            end_date = data.get('end_date'),
            comments = data.get('comments'),
            completed = data.get('completed')
        )

        appointment.save()
        
        return ({'success':True, 'message':'successfully registered company'})