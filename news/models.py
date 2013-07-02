from django.db import models

from node.models import Node, LocalizedNode
from node.views import LocalItem
from tinymce.models import HTMLField
    
class News(Node):
    picture = models.ImageField(upload_to='news/%Y/%m', blank=True, null=True, help_text="Please select a square picture.")
    
    class Meta:
        verbose_name = 'News or Event at NH'
        verbose_name_plural = 'News or Event at NH'
    
    def __unicode__(self):
        local_item = LocalItem(self, LocalizedNews)
        if self.published:
            if local_item:
                return '%s %s' % (self.published.date(), local_item.title)
            else:
                return '%s' % (self.published.date())
        else:
            if local_item:
                return '%s' % (local_item.title)
    
class LocalizedNews(LocalizedNode):
    meta = models.ForeignKey(News)
    title = models.CharField(max_length=63)
    exerpt = models.CharField(max_length=200, blank=True, null=True)
    description = HTMLField(blank=True, null=True)