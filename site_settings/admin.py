from django.contrib import admin

from site_settings.models import Settings, LocalizedSettings
from node.admin import NodeAdmin, LocalizedNodeAdmin

class LocalizedSettingsInline(LocalizedNodeAdmin):
    model = LocalizedSettings
    
class SettingsAdmin(NodeAdmin):
    inlines = [ LocalizedSettingsInline, ]

admin.site.register(Settings, SettingsAdmin)