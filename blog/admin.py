from django.contrib import admin
from django.contrib.auth.models import User

from blog.models import Blog, LocalizedBlog, Author, LocalizedAuthor
from node.admin import NodeAdmin, LocalizedNodeAdmin

class LocalizedBlogInline(LocalizedNodeAdmin):
    model = LocalizedBlog
    
class LocalizedAuthorInline(LocalizedNodeAdmin):
    model = LocalizedAuthor

class AuthorAdmin(NodeAdmin):
    inlines = [ LocalizedAuthorInline, ]

class BlogAdmin(NodeAdmin):
    inlines = [ LocalizedBlogInline, ]

admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
