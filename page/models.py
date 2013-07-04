from django.db import models

from node.models import Node, LocalizedNode
from tinymce.models import HTMLField

class PageCategory(models.Model):
    ABOUTUS = 1
    NEWSandEVENTS = 2
    LOCATIONS = 3
    LANGUAGEARTS = 4
    TESTPREPARATIONS = 5
    CURRICULUMCONSULTING = 6
    LA_INSTRUCTORS = 7
    TP_INSTRUCTORS = 8
    BLOG = 9
    LA_SCHEDULES = 10
    TP_SCHEDULES = 11
    CONTACT = 12
    ADMISSIONSCOUNSELING = 13
    
    name = models.CharField(max_length=63)
    
    def __unicode__(self):
        return '%s' % (self.name)
        
class Page(Node):
    category = models.ForeignKey(PageCategory)
    title = models.CharField(max_length=63)
    priority = models.IntegerField(help_text="'1' means the first item of a list.", default='1000')
    
    def __unicode__(self):
        return '%s: %s' % (self.category, self.title)
    
    class Meta:
        ordering = ['priority']

class LocalizedPage(LocalizedNode):
    meta = models.ForeignKey(Page)
    title = models.CharField(max_length=63, blank=True, null=True)
    subtitle = models.CharField(max_length=127, blank=True, null=True)
    description = HTMLField(blank=True, null=True)
