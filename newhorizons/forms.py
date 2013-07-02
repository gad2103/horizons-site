from datetime import datetime
from django import forms    
from django import template
from django.db import models
from django.utils.translation import ugettext as _

from course.models import TargetCategory, Target, Course, Class
from node.models import Language, DataState
from tinymce.widgets import TinyMCE

class ContactForm(forms.Form):
    REFERENCES = (
        ('friend', 'friend'),
        ('parent', 'parent'),
        ('student', 'student'),
        ('internet article', 'internet article'),
        ('internet advertisement', 'internet advertisement'),
        ('print article', 'print article'),
        ('print advertisement', 'print advertisement'),
        ('other', 'other')
    )
    
    name = forms.CharField(max_length=100)
    sender = forms.EmailField()
    location = forms.CharField(max_length=100)
    language = forms.ModelChoiceField(queryset=Language.objects.all())
    reference = forms.ChoiceField(choices=REFERENCES) 
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, max_length=1000)
    #cc_myself = forms.BooleanField(required=False)


register = template.Library()

@register.inclusion_tag("targetcategory_select.html")
def targetcategory_select():
    targetcategory_list = TargetCategory.objects.all()
    return {'targetcategory_list' : targetcategory_list}    
    
    
class RegisterForm(forms.Form):
    student_name = forms.CharField()
    student_email = forms.EmailField(required=False)
    current_grade = forms.CharField()
    student_mobile = forms.CharField(required=False)
    school = forms.CharField()
    parent_name = forms.CharField()
    parent_email = forms.EmailField()
    preferred_language = forms.ModelChoiceField(queryset=Language.objects.all(), initial=Language.objects.get(pk=Language.DEFAULT))
    parent_mobile = forms.CharField()
    address1 = forms.CharField(required=False)
    address2 = forms.CharField(required=False)
    portals = forms.ModelChoiceField(queryset=TargetCategory.objects.all(), required=False)
    targets = forms.ModelChoiceField(queryset=Target.objects.filter(data_state=DataState.PUBLISHED), required=False)
    courses = forms.ModelChoiceField(queryset=Course.objects.filter(data_state=DataState.PUBLISHED), required=False)
    classes = forms.ModelChoiceField(queryset=Class.objects.filter(data_state=DataState.PUBLISHED, start_time__gt = datetime.now()), required=False, empty_label='next available class')
    
    class Media:
        js = ('registration.js',)

class RegisterForm_target(forms.Form):
    targets = forms.ModelChoiceField(queryset=Target.objects.filter(data_state=DataState.PUBLISHED))
    
    class Media:
        js = ('registration.js',)
    
class RegisterForm_course(forms.Form):
    courses = forms.ModelChoiceField(queryset=Course.objects.filter(data_state=DataState.PUBLISHED))
    
    class Media:
        js = ('registration.js',)

class RegisterForm_class(forms.Form):
    classes = forms.ModelChoiceField(queryset=Class.objects.filter(data_state=DataState.PUBLISHED, start_time__gt = datetime.now()), required=False, empty_label='next available class')
    
    class Media:
        js = ('registration.js',)
    