from django.contrib import admin
from service.models import Service
from service.models import Reminder

class ServiceAdmin(admin.ModelAdmin):
    list_display=('box_number','medicine_name','quantity')

admin.site.register(Service,ServiceAdmin) 
# Register your models here.
class ReminderAdmin(admin.ModelAdmin):
    list_display=('medicine_name','time_to_take_medicine')

admin.site.register(Reminder,ReminderAdmin)