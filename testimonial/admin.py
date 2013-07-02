from django.contrib import admin

from testimonial.models import Testimonial, LocalizedTestimonial
from node.admin import NodeAdmin, LocalizedNodeAdmin

class LocalizedTestimonialInline(LocalizedNodeAdmin):
    model = LocalizedTestimonial
    
class TestimonialAdmin(NodeAdmin):
    inlines = [ LocalizedTestimonialInline, ]

admin.site.register(Testimonial, TestimonialAdmin)