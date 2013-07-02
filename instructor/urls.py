from django.conf.urls import patterns, url, include
from django.views.generic.simple import redirect_to

from course.models import TargetCategory

urlpatterns = patterns('instructor.views',
    url(r'^$', redirect_to, {'url': '/instructors/testprep'}, name='instructor_home'),
    url(r'^testprep$', 'index', {'type' : TargetCategory.TESTPREPARATIONS}, name='tp_home_instructors'),
    url(r'^languagearts$', 'index', {'type' : TargetCategory.LANGUAGEARTS}, name='la_home_instructors'),
    url(r'^curriculumconsulting$', 'index', {'type' : TargetCategory.CURRICULUMCONSULTING}, name='cc_home_instructors'),
    
    url(r'^details/(?P<target>\d+)(?:/(?P<course>\d+))?$', 'details', name='instructor_details'), #the identifier is a course.pk
    url(r'^details$', 'details', name='instructor_details_all'),
    
    url(r'^navigation(?:/(?P<identifier>\d+))?$', 'navigation', name='instructor_navigation'),
    url(r'^la_navigation(?:/(?P<identifier>\d+))?$', 'navigation', {'type' : TargetCategory.LANGUAGEARTS}, name='la_nav_instructors'),
    url(r'^tp_navigation(?:/(?P<identifier>\d+))?$', 'navigation', {'type' : TargetCategory.TESTPREPARATIONS}, name='tp_nav_instructors'),
    url(r'^cc_navigation(?:/(?P<identifier>\d+))?$', 'navigation', {'type' : TargetCategory.CURRICULUMCONSULTING}, name='cc_nav_instructors'),
    
    url(r'^languagearts/list$', 'list', {'type' : TargetCategory.LANGUAGEARTS}, name='la_instructor_list'),
    url(r'^testprep/list$', 'list', {'type' : TargetCategory.TESTPREPARATIONS}, name='tp_instructor_list'),
)
