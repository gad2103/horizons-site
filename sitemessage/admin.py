from django.contrib import admin

from sitemessage.models import SiteMessage, LocalizedSiteMessage

class LocalizedSiteMessageInline(admin.StackedInline):
    model = LocalizedSiteMessage
    fk_name = 'meta'
    extra = 3
    max_num = 3
    
class SiteMessageAdmin(admin.ModelAdmin):
    inlines = [ LocalizedSiteMessageInline, ]

admin.site.register(SiteMessage, SiteMessageAdmin)