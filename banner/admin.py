from django.contrib import admin

from banner.models import Banner, LocalizedBanner
from node.admin import NodeAdmin, LocalizedNodeAdmin

class LocalizedBannerInline(LocalizedNodeAdmin):
    model = LocalizedBanner
    
class BannerAdmin(NodeAdmin):
    
    inlines = [ LocalizedBannerInline, ]

admin.site.register(Banner, BannerAdmin)