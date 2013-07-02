from django.db import models

from node.models import Node, LocalizedNode
from tinymce.models import HTMLField
    
class Inthenews(Node):
    picture = models.FileField(upload_to="inthenews_picture/%Y/%m", blank=True, null=True)
    source = models.CharField(max_length=63)
    title = models.CharField(max_length=63)
    exerpt = models.CharField(max_length=511, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to="inthenews_file/%Y/%m", blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'News Clips'
    
    def __unicode__(self):
        return '%s (%s)' % (self.source, self.pk)
        
    def save(self, *args, **kwargs):
        super(Inthenews, self).save(*args, **kwargs)