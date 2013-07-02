from django.contrib import admin

from blog.models import Blog, LocalizedBlog
from node.admin import NodeAdmin, LocalizedNodeAdmin

class LocalizedBlogInline(LocalizedNodeAdmin):
    model = LocalizedBlog
    
class BlogAdmin(NodeAdmin):
    inlines = [ LocalizedBlogInline, ]

admin.site.register(Blog, BlogAdmin)
