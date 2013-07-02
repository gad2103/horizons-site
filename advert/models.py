from django.db import models

from node.models import Node

class AdvertCategory(models.Model):
    GENERAL = 1
    LA_COURSE = 2
    TP_COURSE = 3

    name = models.CharField(max_length=63)   
    
    class Meta:
        verbose_name_plural = 'Advert categories'
    
    def __unicode__(self):
        return '%s' % (self.name) 
    
class Advert(Node):
    name = models.CharField(max_length=63) 
    category = models.ForeignKey(AdvertCategory)
    url = models.URLField()
    picture = models.ImageField(upload_to='advert/%Y/%m')
    
    def __unicode__(self):
        return '%s: %s' % (self.category, self.pk)