from django.contrib import admin

from inthenews.models import Inthenews
from node.admin import NodeAdmin

class InthenewsAdmin(NodeAdmin):
    pass

admin.site.register(Inthenews, InthenewsAdmin)