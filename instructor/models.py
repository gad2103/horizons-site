from django.db import models

from node.models import Node, LocalizedNode, Language
from tinymce.models import HTMLField

class Instructor(Node):
    picture = models.ImageField(upload_to='instructors', blank=True, null=True)
    topics = models.ManyToManyField('course.Course')
    priority = models.IntegerField(help_text="'1' means the first item of a list.", default='1000')
    
    def __unicode__(self):
        try:
            Loc = LocalizedInstructor.objects.get(meta__pk = self.pk, language=Language.DEFAULT)
            return '%s, %s' % (Loc.last_name, Loc.first_name)
        except LocalizedNode.DoesNotExist:
            return '%s' % (self.pk)
            
    class Meta:
        ordering = ['priority']

class LocalizedInstructor(LocalizedNode):
    meta = models.ForeignKey(Instructor)
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    description = HTMLField(blank=True, null=True)
    
    def __unicode__(self):
        return '%s, %s' % (self.last_name, self.first_name)
