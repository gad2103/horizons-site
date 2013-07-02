from django.db import models
from node.models import Node, LocalizedNode
from tinymce.models import HTMLField

class Settings(Node):
    name = models.CharField(max_length=127, blank=True, null=True)
    analytics = models.CharField(max_length=1024, blank=True, null=True, help_text="Do not include &lt;script&gt;&lt;/script&gt; tags.")
    favicon = models.ImageField(upload_to='favicon', blank=True, null=True)
    
    def __unicode__(self):
        return '%s' % (self.name)
        
    class Meta:
        verbose_name = 'Header, Footer, Analytics' 
        verbose_name_plural = 'Header, Footer, Analytics'
    
class LocalizedSettings(LocalizedNode):
    meta = models.ForeignKey(Settings)
    moto = models.CharField(max_length=127, blank=True, null=True)
    copyrights = models.CharField(max_length=127, blank=True, null=True)
    contact_footer = HTMLField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Localized Footer'
        verbose_name_plural = 'Localized Footer'
