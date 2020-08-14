import datetime
from rest_framework import serializers
from datetime import date
from .models import Appointment
from rest_framework.response import Response


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'start_date', 'end_date', 'comments', 'completed')

    def is_time_between(self, begin_time, end_time):
        _check_time_am = datetime.time(9,00,00)
        _check_time_pm = datetime.time(17,00,00)
        
        if (begin_time < _check_time_am) & (end_time > _check_time_pm):
            return False
        else:
            return True

    def create(self, validated_data):
        
        data = validated_data
        
        
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        start_time = start_date.time()
        end_time = end_date.time()

        if start_date.weekday() & end_date.weekday() & self.is_time_between(start_time, end_time):
            appointment = Appointment.objects.create(       
                patient = data.get('patient'),
                start_date = data.get('start_date'),
                end_date = data.get('end_date'),
                comments = data.get('comments'),
                completed = data.get('completed')
            )

            appointment.save()
        
            return ({'success':True, 'message':'successfully registered company'})
        else:
            return ({'success':False, 'message':'Please create an appointment within the weekdays and 9AM-5PM.'})


        