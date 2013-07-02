from django.db import models

from node.models import Node, LocalizedNode
from tinymce.models import HTMLField

class Location(Node):
    picture = models.ImageField(upload_to='locations', blank=True, null=True)
    name = models.CharField(max_length=63)
    priority = models.IntegerField(help_text="'1' means the first item of a list.", default='1000')
    file = models.FileField(upload_to="locations/%Y/%m", blank=True, null=True)
    
    def __unicode__(self):
        return '%s' % (self.name)
    
    class Meta:
        ordering = ['priority']

class LocalizedLocation(LocalizedNode):
    meta = models.ForeignKey(Location)
    name = models.CharField(max_length=63)
    address = HTMLField()
    directions = HTMLField(blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    
    def __unicode__(self):
        return '%s' % (self.name)
