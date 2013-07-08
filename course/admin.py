from django.contrib import admin

from course.models import TargetCategory, LocalizedTargetCategory
from course.models import Target, LocalizedTarget
from course.models import Course, LocalizedCourse
from course.models import Class
from course.models import Weblink
from node.admin import NodeAdmin, LocalizedNodeAdmin

class LocalizedTargetCategoryInline(LocalizedNodeAdmin):
    model = LocalizedTargetCategory

class LocalizedTargetInline(LocalizedNodeAdmin):
    model = LocalizedTarget

class LocalizedCourseInline(LocalizedNodeAdmin):
    model = LocalizedCourse
    
class TargetCategoryAdmin(NodeAdmin):
    inlines = [ LocalizedTargetCategoryInline, ]
    
class TargetAdmin(NodeAdmin):
    inlines = [ LocalizedTargetInline, ]
    
class CourseAdmin(NodeAdmin):
    inlines = [ LocalizedCourseInline, ]


admin.site.register(TargetCategory, TargetCategoryAdmin)
admin.site.register(Target, TargetAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Class)
admin.site.register(Weblink)
