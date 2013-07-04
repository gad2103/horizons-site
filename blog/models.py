from django.db import models

from node.models import Node, LocalizedNode, Language
from node.views import LocalItem
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Blog(Node):
    picture = models.ImageField(upload_to='blog/%Y/%m', blank=True, null=True, help_text="Please select a square picture.")
    author = models.ForeignKey(User)
    
    def __unicode__(self):
        local_item = LocalItem(self, LocalizedBlog)
        if self.published:
            if local_item:
                return u'%s %s' % (self.published.date(), local_item.title)
            else:
                return u'%s' % (self.published.date())
        else:
            if local_item:
                return u'%s' % (local_item.title)
    
class LocalizedBlog(LocalizedNode):
    meta = models.ForeignKey(Blog)
    title = models.CharField(max_length=63)
    exerpt = models.CharField(max_length=511, blank=True, null=True)
    description = HTMLField(blank=True, null=True)
        
    #def save(self, *args, **kwargs):
    #    # Strip inline styles from the TinyMCE 'description' field.
    #    p = re.compile(" style=\".*?\"")
    #    for item in self.__dict__:
    #        if item == 'description':
    #            self.__dict__[item] = p.sub('', self.__dict__[item])
    #    super(LocalizedCourse, self).save(*args, **kwargs)
