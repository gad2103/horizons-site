from django.db import models

from node.models import Node, LocalizedNode
from tinymce.models import HTMLField

class TestimonialCategory(models.Model):
    GENERAL = 1
    LANGUAGEARTS = 2
    TESTPREPARATIONS = 3
    CURRICULUMCONSULTING = 4

    name = models.CharField(max_length=63)   
    
    class Meta:
        verbose_name_plural = 'Testimonial categories'
    
    def __unicode__(self):
        return '%s' % (self.name) 
    
class Testimonial(Node):
    category = models.ForeignKey(TestimonialCategory)
    priority = models.IntegerField(help_text="'1' means the first item of a list.", default='1000')
    
    def __unicode__(self):
        return '%s: %s' % (self.category, self.pk)
        
    class Meta:
        ordering = ['priority']
    
class LocalizedTestimonial(LocalizedNode):
    meta = models.ForeignKey(Testimonial)
    created_by = HTMLField(blank=True, null=True)
    exerpt = models.CharField(max_length=200, blank=True, null=True)
    description = HTMLField(blank=True, null=True)
        
    def save(self, *args, **kwargs):
        super(LocalizedTestimonial, self).save(*args, **kwargs)
