from django.contrib import admin

from webapp.models import City, Event, Location
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')

class LocationAdmin(admin.ModelAdmin):
    list_display =  ('name', 'city')

admin.site.register(City)
admin.site.register(Location, LocationAdmin)
admin.site.register(Event, EventAdmin)
