from django.contrib import admin

from advert.models import Advert
from node.admin import NodeAdmin

class AdvertAdmin(NodeAdmin):
    pass
    
admin.site.register(Advert, AdvertAdmin)