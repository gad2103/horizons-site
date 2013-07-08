from django.db import models

from instructor.models import Instructor
from location.models import Location
from node.models import Node, LocalizedNode, Language
from tinymce.models import HTMLField

class TargetCategory(models.Model):
    TESTPREPARATIONS = 1
    LANGUAGEARTS = 2
    CURRICULUMCONSULTING = 3
    ADMISSIONSCOUNSELING=7
    
    name = models.CharField(max_length=63)
    picture = models.ImageField(upload_to='portals', blank=True, null=True)
    priority = models.IntegerField(help_text="'1' means the first item of a list.", default='1000')
    
    def __unicode__(self):
        return '%s' % (self.name)
        
    class Meta:
        verbose_name = 'Division'
        ordering = ['priority']
        
class LocalizedTargetCategory(models.Model):
    meta = models.ForeignKey(TargetCategory)
    language = models.ForeignKey(Language, related_name="portal localization language")
    intro = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Localized Division'
        verbose_name_plural = 'Localized Divisions'
    
class Target(Node):
    name = models.CharField(max_length=31)
    shortname = models.CharField(max_length=15)
    category = models.ForeignKey(TargetCategory, verbose_name='division')
    priority = models.IntegerField(help_text="'1' means the first item of a list.", default='1000')
    
    def __unicode__(self):
        return '%s' % (self.name)
        
    class Meta:
        verbose_name = 'Program'
        ordering = ['priority']
    
class LocalizedTarget(LocalizedNode):
    meta = models.ForeignKey(Target)
    description = HTMLField(blank=True, null=True)
    
    class Meta:
        verbose_name = 'Localized Program'
        verbose_name_plural = 'Localized Programs'

class Course(Node):
    target = models.ForeignKey(Target)
    name = models.CharField(max_length=63, verbose_name='program')
    priority = models.IntegerField(help_text="'1' means the first item of a list.", default='1000')
    
    def __unicode__(self):
        return '%s %s' % (self.target.shortname, self.name)
        
    class Meta:
        ordering = ['priority']

class LocalizedCourse(LocalizedNode):
    meta = models.ForeignKey(Course)
    description = HTMLField(blank=True, null=True)
    skills = models.CharField(max_length=63, blank=True, null=True, help_text="comma separated list")

class Class(Node):
    course = models.ForeignKey(Course)
    code = models.CharField("course code", max_length=31)
    start_time = models.DateField()
    end_time = models.DateField()
    schedule = models.FileField(upload_to="schedules/%Y/%m", blank=True, null=True)
    location = models.ManyToManyField(Location, blank=True, null=True)
    priority = models.IntegerField(help_text="'1' means the first item of a list.", default='1000')
    
    class Meta:
        verbose_name_plural = 'Classes'
        ordering = ['start_time', 'location__priority']
        
    def get_locations(self):
        return ", ".join([l.name for l in self.location.all()])

    def __unicode__(self):
        DATE_FORMAT = "%Y-%m-%d"
        TIME_FORMAT = "%H:%M:%S"
        
        if self.schedule==None:
            return '%s - %s %s (no schedule file) at %s' % (self.code, self.course, self.pk, self.get_locations())
        else:
            return '%s - %s %s at %s' % (self.code, self.course, self.pk, self.get_locations())
        #if self.schedule==None:
        #    return '%s %s (no schedule file) at %s' % (self.course, self.pk, self.location)
        #else:
        #    return '%s %s at %s' % (self.course, self.pk, self.location)

class Weblink(models.Model):
    name = models.CharField(max_length=127)
    url  = models.URLField(blank=True, null=True)
    courses = models.ManyToManyField(Course, blank=True, null=True)
    priority = models.IntegerField(help_text="'1' means the first item of a list.", default='1000')
    
    def __unicode__(self):
        return '%s: %s' % (self.name, self.url)
        
    class Meta:
        ordering = ['priority']
