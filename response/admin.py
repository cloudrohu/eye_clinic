from django.contrib import admin
from .models import *

# Register your models here.

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'phone','created_at','updated_at',)
admin.site.register(Response, ResponseAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'email', 
        'phone', 
        'appointment_date', 
        'submitted_at'
    )
    list_filter = ('appointment_date', 'submitted_at')
    search_fields = ('name', 'email', 'phone')
    date_hierarchy = 'appointment_date'


admin.site.register(Appointment, AppointmentAdmin)
