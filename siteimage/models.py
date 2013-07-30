from django.db import models
    
class SiteImageCategory(models.Model):
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
    AC_COURSE = 13

    name = models.CharField(max_length=63)   
    
    class Meta:
        verbose_name_plural = 'Site image categories'
    
    def __unicode__(self):
        return '%s' % (self.name)


class SiteImage(models.Model):
    category = models.ForeignKey(SiteImageCategory)
    name = models.CharField(max_length=127)
    picture = models.ImageField(upload_to='site_images/%Y/%m')
    
    def __unicode__(self):
        return '%s: %s' % (self.category.name, self.name)
