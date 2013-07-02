from django.db import models

from node.models import Node, LocalizedNode, Language
from node.views import LocalItem
from tinymce.models import HTMLField
    
class SiteMessage(models.Model):
    name = models.CharField(max_length=127)
    
    def __unicode__(self):
        local_item = LocalItem(self, LocalizedSiteMessage)
        return '%s' % (self.name)
    
class LocalizedSiteMessage(models.Model):
    meta = models.ForeignKey(SiteMessage)
    language = models.ForeignKey(Language, related_name="site message localization language")
    text = HTMLField(blank=True, null=True)