from django.contrib import admin

from location.models import Location, LocalizedLocation
from node.admin import NodeAdmin, LocalizedNodeAdmin

class LocalizedLocationInline(LocalizedNodeAdmin):
    model = LocalizedLocation
    fields = ('language', 'name', 'description', 'directions')
    
class LocationAdmin(NodeAdmin):
    inlines = [ LocalizedLocationInline, ]

admin.site.register(Location, LocationAdmin)