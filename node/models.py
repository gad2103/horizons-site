import datetime, re
from django.contrib.contenttypes.models import ContentType
from django.db import models

# For AdminImageWidget
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
import os
import Image

class DataState(models.Model):
    SUBMITTED = 1
    PUBLISHED = 2
    FLAGGED = 3
    CLOSED = 4
    DELETED = 5
    
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return unicode(self.name) or u''
    
    class Meta:
        app_label = 'node'

class Node(models.Model):
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)
    published = models.DateTimeField(blank=True, null=True, default=datetime.datetime.today())
    
    data_state = models.ForeignKey('node.DataState', default=DataState.SUBMITTED)
    content_type = models.ForeignKey(ContentType,editable=False,null=True)
    
    def __unicode__(self):
        #return '%s' % (self.pk)
        return unicode(self.pk) or u''

    '''def __init__(self, *args, **kwargs):
        if self.__class__.__name__ == "Author":
            self._meta.get_field('data_state').default = DataState.PUBLISHED
        else:
            self._meta.get_field('data_state').default = DataState.SUBMITTED
        super(Node,self).__init__(*args, **kwargs)'''
        
    def save(self, request=None, *args, **kwargs):
        self.modified = datetime.datetime.today()
        #if request :
        #    self.modifier = request.user
        #    try: 
        #        self.creator = self.creator
        #    except ObjectDoesNotExist:
        #        self.creator = request.user
        #import pdb; pdb.set_trace()
        try:
            existing = Node.objects.get(pk=self.pk)
            if existing.data_state.pk!=DataState.PUBLISHED and self.data_state.pk==DataState.PUBLISHED:
                self.published=datetime.datetime.today()
        except Node.DoesNotExist:
            self.created = datetime.datetime.today()
            if self.data_state.pk==DataState.PUBLISHED:
                self.published=datetime.datetime.today()
        
        if(not self.content_type):
            self.content_type = ContentType.objects.get_for_model(self.__class__)
        
        models.Model.save(self, *args, **kwargs)
    
class Language(models.Model):
    DEFAULT = 12 # English Language as defined in fixtures/initial_data.json
    PRIORITY = list([12,70,39]) # English, Simplified Chinese, Korean
    
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10)
    
    def __unicode__(self):
        #return '%s' % (self.name)
        return unicode(self.name) or u''
    
    @classmethod    
    def get_language(self, request=None):
        if request:
            try:
                language = Language.objects.get(code = request.session['django_language'])
            except:
                language = Language.objects.get(pk=Language.DEFAULT)
        else:
            language = Language.objects.get(pk=Language.DEFAULT)
            
        return language
        
class LocalizedNode(Node):
    language = models.ForeignKey(Language, related_name="localization language")
    
    def __unicode__(self):
        #return '%s' % (self.pk)
        return unicode(self.pk) or u''
        
class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
                
            image_url = value.url
            file_name=str(value)
            
            # defining the size
            size='100x100'
            x, y = [int(x) for x in size.split('x')]
            
            # defining the filename and the miniature filename
            filehead, filetail 	= os.path.split(value.path)
            basename, format 	= os.path.splitext(filetail)
            miniature 		= basename + '_' + size + format
            filename 		= value.path
            miniature_filename 	= os.path.join(filehead, miniature)
            filehead, filetail 	= os.path.split(value.url)
            miniature_url 		= filehead + '/' + miniature
            
            # make sure that the thumbnail is a version of the current original sized image
            if os.path.exists(miniature_filename) and os.path.getmtime(filename) > os.path.getmtime(miniature_filename):
                os.unlink(miniature_filename)
                    
            # if the image wasn't already resized, resize it
            if not os.path.exists(miniature_filename):
                image = Image.open(filename)
                image.thumbnail([x, y], Image.ANTIALIAS)
                try:
                        image.save(miniature_filename, image.format, quality=100, optimize=1)
                except:
                        image.save(miniature_filename, image.format, quality=100)
            
            output.append(u' <div><a href="%s" target="_blank"><img src="%s" alt="%s" /></a></div> %s ' % \
            (miniature_url, miniature_url, miniature_filename, _('Change:')))
                
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))
