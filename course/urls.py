from django.conf.urls import patterns, url, include
from django.views.generic.simple import redirect_to

from course.models import TargetCategory
from page.models import PageCategory

urlpatterns = patterns('course.views',
    url(r'^(?P<identifier>\d+)$', 'index_redirect', name='course_home'),
    url(r'^testprep(?:/(?P<identifier>\d+))?$', 'index', {'type' : TargetCategory.TESTPREPARATIONS}, name='testpreparations_home'),
    url(r'^languagearts(?:/(?P<identifier>\d+))?$', 'index', {'type' : TargetCategory.LANGUAGEARTS}, name='languagearts_home'),
    url(r'^curriculumconsulting$', 'index', {'type' : TargetCategory.CURRICULUMCONSULTING}, name='curriculumconsulting_home'),
    url(r'^admissionscounseling$', 'index', {'type' : TargetCategory.ADMISSIONSCOUNSELING}, name='admissionscounseling_home'), 
    url(r'^testprep/schedule$',            'schedule',   {'type': TargetCategory.TESTPREPARATIONS}, name='testprep_schedule'),
    url(r'^languagearts/schedule$',        'schedule',   {'type': TargetCategory.LANGUAGEARTS}, name='languagearts_schedule'),
    url(r'^testprep/schedule/nav$',        'navigation', {'type' : TargetCategory.TESTPREPARATIONS, 'area' : 'schedule'}, name='testprep_schedule_nav'),
    url(r'^languagearts/schedule/nav$',    'navigation', {'type' : TargetCategory.LANGUAGEARTS, 'area' : 'schedule'}, name='languagearts_schedule_nav'),
    url(r'^schedule/(?P<target>\d+)(?:/(?P<course>\d+))?$', 'class_list', name='schedule_list'), 
    url(r'^target_details/(?P<identifier>\d+)$', 'target_details', name='target_details'),
    url(r'^target_details$', 'target_details', name='target_details_all'),
    #url(r'^target_details(?:/(?P<language>[a-zA-Z]+))?$', 'target_details', name='target_details_all'),
    url(r'^course_details/(?P<identifier>\d+)$', 'course_details', name='course_details'),
    url(r'^course_details$', 'course_details', name='course_details_all'),
    url(r'^navigation(?:/(?P<identifier>\d+))?$', 'navigation', name='course_navigation'),
    url(r'^la_navigation$', 'navigation', {'type' : TargetCategory.LANGUAGEARTS}, name='languagearts_nav'),
    url(r'^tp_navigation$', 'navigation', {'type' : TargetCategory.TESTPREPARATIONS}, name='testprep_nav'),
    url(r'^cc_navigation$', 'navigation', {'type' : TargetCategory.CURRICULUMCONSULTING}, name='curriculumconsulting_nav'),
    url(r'^ac_navigation$', 'navigation', {'type' : TargetCategory.ADMISSIONSCOUNSELING}, name='admissions_nav'),

    # The URLs for the the current and upcoming classes mini panels
    url(r'^current_classes$', 'current_classes', name='current_classes'),
    url(r'^upcoming_classes$', 'upcoming_classes', name='upcoming_classes'),
    url(r'^current_tp_classes(?:/(?P<course>\d+))?$', 'current_classes', {'type' : TargetCategory.TESTPREPARATIONS},   name='current_tp_classes'),
    url(r'^upcoming_tp_classes(?:/(?P<course>\d+))?$', 'upcoming_classes', {'type' : TargetCategory.TESTPREPARATIONS}, name='upcoming_tp_classes'),
    url(r'^current_la_classes(?:/(?P<course>\d+))?$', 'current_classes', {'type' : TargetCategory.LANGUAGEARTS},   name='current_la_classes'),
    url(r'^upcoming_la_classes(?:/(?P<course>\d+))?$', 'upcoming_classes', {'type' : TargetCategory.LANGUAGEARTS}, name='upcoming_la_classes'),
    url(r'^upcoming_la_classes_preview$', 'class_preview', {'type' : TargetCategory.LANGUAGEARTS},     name='upcoming_la_classes_schedule_preview'),
    url(r'^upcoming_tp_classes_preview$', 'class_preview', {'type' : TargetCategory.TESTPREPARATIONS}, name='upcoming_tp_classes_schedule_preview'),
    
    url(r'^course_link_list/(?P<identifier>\d+)$', 'course_link_list', name='course_link_list'),
    url(r'^target_link_list/(?P<identifier>\d+)$', 'target_link_list', name='target_link_list'),
)
