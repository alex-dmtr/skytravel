from django.contrib import admin

from webapp.models import City, Event, Location
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')


admin.site.register(City)
admin.site.register(Location)
admin.site.register(Event, EventAdmin)
