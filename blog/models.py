from django.db import models

from node.models import Node, LocalizedNode, Language
from node.views import LocalItem
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Author(Node):
    #author = models.ForeignKey(User, blank=True, null=True, related_name='+')
    picture = models.ImageField(upload_to='authors', blank=True, null=True)
    def __unicode__(self):
        try:
            Loc = LocalizedAuthor.objects.get(meta__pk = self.pk, language=Language.DEFAULT)
            return u'%s, %s' % (Loc.last_name, Loc.first_name)
        except LocalizedNode.DoesNotExist:
            return u'%s' % (self.pk)
    def __init__(self, *args, **kwargs):
        self._meta.get_field('data_state').default = 2
        self._meta.get_field('data_state').editable = False
        super(Author, self).__init__(*args, **kwargs)

class LocalizedAuthor(LocalizedNode):
    meta = models.ForeignKey(Author)
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    description = HTMLField(blank=True, null=True)
    
    def __unicode__(self):
        return '%s, %s' % (self.last_name, self.first_name)
        
class Blog(Node):
    picture = models.ImageField(upload_to='blog/%Y/%m', blank=True, null=True, help_text="Please select a square picture.")
    created_by = models.ForeignKey(Author, blank=True, null=True)
    
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
