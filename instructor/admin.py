from django.contrib import admin

from instructor.models import Instructor, LocalizedInstructor
from node.admin import NodeAdmin, LocalizedNodeAdmin

class LocalizedInstructorInline(LocalizedNodeAdmin):
    model = LocalizedInstructor
    fields = (('data_state', 'language'), ('last_name', 'first_name'), 'description')
    
    class Meta:
        js = ("admin.js")
    
class InstructorAdmin(NodeAdmin):
    inlines = [ LocalizedInstructorInline, ]

admin.site.register(Instructor, InstructorAdmin)