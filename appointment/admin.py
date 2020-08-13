from django.contrib import admin
from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'start_date', 'end_date', 'comments')


admin.site.register(Appointment, AppointmentAdmin)
