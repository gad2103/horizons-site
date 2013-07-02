from django.contrib import admin

from news.models import News, LocalizedNews
from node.admin import NodeAdmin, LocalizedNodeAdmin

class LocalizedNewsInline(LocalizedNodeAdmin):
    model = LocalizedNews
    
class NewsAdmin(NodeAdmin):
    inlines = [ LocalizedNewsInline, ]

admin.site.register(News, NewsAdmin)