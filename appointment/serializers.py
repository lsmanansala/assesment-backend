import datetime
from rest_framework import serializers
from datetime import date
from .models import Appointment
from rest_framework.response import Response


class AppointmentSerializer(serializers.ModelSerializer):
    """
    Serializer class for Appointments
    """
    
    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'start_date', 'end_date', 'comments', 'completed')

    def is_time_between(self, begin_time, end_time):
        """
        Check if the time given is between 9am and 5pm
        """
        _check_time_am = datetime.time(9,00,00)
        _check_time_pm = datetime.time(17,00,00)

        if (begin_time < _check_time_am) & (end_time > _check_time_pm):
            return False
        else:
            return True

    def create(self, validated_data):
        """
        Override create function to check first the start and end date of each appointment
        """
        
        data = validated_data
        
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        start_time = start_date.time()
        end_time = end_date.time()

        #restricting bookings that is not a weekday and not between 9AM and 5PM
        if start_date.weekday() & end_date.weekday(): 
            
            if self.is_time_between(start_time, end_time):

                _appointment = Appointment.objects.filter(start_date=start_date)
                if _appointment: # check if there is an appointment already created for the date and time specified
                    return ({'success':False, 'message':'There is an appointment created for this date and time'})
                else:
                    appointment = Appointment.objects.create(       
                        patient = data.get('patient'),
                        start_date = data.get('start_date'),
                        end_date = data.get('end_date'),
                        comments = data.get('comments'),
                        completed = data.get('completed')
                    )
                    appointment.save()
                    return ({'success':True, 'message':'successfully registered company'})
            return ({'success':False, 'message':'Please create an appointment within the weekdays and 9AM-5PM.'})
        else:
            return ({'success':False, 'message':'Please create an appointment within the weekdays and 9AM-5PM.'})


        