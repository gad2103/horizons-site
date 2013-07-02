from django.contrib import admin

from page.models import Page, LocalizedPage
from node.admin import NodeAdmin, LocalizedNodeAdmin

class LocalizedPageInline(LocalizedNodeAdmin):
    model = LocalizedPage
    
class PageAdmin(NodeAdmin):
    inlines = [ LocalizedPageInline, ]

admin.site.register(Page, PageAdmin)