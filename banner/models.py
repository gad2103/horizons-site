from django.db import models

from node.models import Node, LocalizedNode

class BannerCategory(models.Model):
    HOME = 1
    LA_COURSE = 2
    TP_COURSE = 3
    CC_COURSE = 4
    LA_INSTRUCTORS = 5
    TP_INSTRUCTORS = 6
    NEWS_EVENTS = 7
    LOCATIONS = 8
    ABOUT = 9
    BLOG = 10
    LA_SCHEDULE = 11
    TP_SCHEDULE = 12
    CONTACT = 13
    REGISTRATION = 14

    name = models.CharField(max_length=63)   
    
    class Meta:
        verbose_name_plural = 'Banner categories'
    
    def __unicode__(self):
        return '%s' % (self.name) 
    
class Banner(Node):
    category = models.ForeignKey(BannerCategory)
    picture = models.ImageField(upload_to='banners/%Y/%m', help_text='Dimensions should be 960x220px.')
    priority = models.IntegerField(help_text="'1' means the first item of a list.", default='1000')
    
    def __unicode__(self):
        return '%s: %s' % (self.category, self.pk) 
    
class LocalizedBanner(LocalizedNode):
    meta = models.ForeignKey(Banner)
    description = models.CharField(max_length=127, verbose_name='overlay text')