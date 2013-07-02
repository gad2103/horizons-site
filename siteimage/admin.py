from django.contrib import admin

from siteimage.models import SiteImage, SiteImageCategory
from node.admin import NodeAdmin
    
class SiteImageAdmin(NodeAdmin):
    pass

admin.site.register(SiteImage, SiteImageAdmin)