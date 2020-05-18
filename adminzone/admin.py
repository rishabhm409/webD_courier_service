from django.contrib import admin
from .models import Qualification,City,Notification,Packet
# Register your models here.
admin.site.register(Qualification)
admin.site.register(City)
admin.site.register(Notification)
admin.site.register(Packet)