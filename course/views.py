import sys, re
from datetime import datetime
from django.core.urlresolvers import reverse
from django.db import models
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.utils.translation import ugettext as _

from banner.models import BannerCategory
from course.models import Target, TargetCategory, LocalizedTarget, Course, LocalizedCourse, Weblink, Class
from newhorizons.views import news_list, blog_list, getBanners
from node.models import Language, DataState
from node.views import Paginate, LocalSet
from siteimage.models import SiteImage, SiteImageCategory
from sitemessage.views import get_message
    
def index_redirect(request, identifier):
    a_course = Course.objects.get(pk=identifier)
    type = a_course.target.category.pk
    if type == TargetCategory.TESTPREPARATIONS:
        next_page = reverse('testpreparations_home', kwargs={'type': type, 'identifier': identifier})
    elif type == TargetCategory.LANGUAGEARTS:
        next_page = reverse('languagearts_home', kwargs={'type': type, 'identifier': identifier})
    
    return HttpResponseRedirect(next_page)
    
def index(request, type=None, identifier=None):
    initializer = {}
    response_payload = {}
    if type == TargetCategory.TESTPREPARATIONS:
        template = 'courses/index_tp.html'
        banners = getBanners(request, BannerCategory.TP_COURSE)
        try:
            left_nav_image = SiteImage.objects.get(category=SiteImageCategory.TP_COURSE)
        except Exception:
            left_nav_image = None
        initializer['nav_url'] = reverse('testprep_nav')
        if identifier:
            the_target = Course.objects.get(pk=identifier).target
            back_link = reverse('testpreparations_home')
            #initializer['header_text'] = "<a href=&quot;" + back_link + "&quot;>" + the_target.category.name + "</a> > " + the_target.name
            initializer['header_text'] = the_target.category.name+" > "+the_target.name
            initializer['content_url'] = reverse('course_details', kwargs={'identifier': identifier})
        else:
            initializer['header_text'] = _('test preparation')
            initializer['content_url'] = reverse('tp_home_page')
        initializer['current_classes_url'] = reverse('current_tp_classes')
        initializer['upcoming_classes_url'] = reverse('upcoming_tp_classes')
    elif type == TargetCategory.LANGUAGEARTS:
        template = 'courses/index_la.html'
        banners = getBanners(request, BannerCategory.LA_COURSE)
        try:
            left_nav_image = SiteImage.objects.get(category=SiteImageCategory.LA_COURSE)
        except Exception:
            left_nav_image = None
        initializer['nav_url'] = reverse('languagearts_nav')
        if identifier:
            the_target = Course.objects.get(pk=identifier).target
            back_link = reverse('languagearts_home')
            #initializer['header_text'] = '<a href=&quot;' + back_link + '&quot;>' + the_target.category.name + '</a> > ' + the_target.name
            initializer['header_text'] = the_target.category.name+" > "+the_target.name
            initializer['content_url'] = reverse('target_details', kwargs={'identifier': Course.objects.get(pk=identifier).target.pk})
        else:
            initializer['header_text'] = _('language arts')
            initializer['content_url'] = reverse('la_home_page')
        initializer['current_classes_url'] = reverse('current_la_classes')
        initializer['upcoming_classes_url'] = reverse('upcoming_la_classes')
    elif type ==  TargetCategory.CURRICULUMCONSULTING:
        template = 'courses/index_cc.html'
        banners = getBanners(request, BannerCategory.CC_COURSE)
        try:
            left_nav_image = SiteImage.objects.get(category=SiteImageCategory.CC_COURSE)
        except Exception:
            left_nav_image = None
        initializer['header_text'] = _('curriculum consulting')
        initializer['content_url'] = reverse('cc_home_page')
    elif type ==  TargetCategory.ADMISSIONSCOUNSELING:
        template = 'courses/index_ac.html'
        banners = getBanners(request, BannerCategory.AC_COURSE)
        try:
            left_nav_image = SiteImage.objects.get(category=SiteImageCategory.AC_COURSE)
        except Exception:
            left_nav_image = None
        initializer['header_text'] = _('admissions counseling')
        initializer['content_url'] = reverse('ac_home_page')
        initializer['nav_url'] = reverse('admissions_nav')
    else:
        template = 'courses/index.html'
        banners = None
    if type == TargetCategory.ADMISSIONSCOUNSELING or type == TargetCategory.CURRICULUMCONSULTING:
        response_payload['blog_list'] = blog_list(request, 5)
        response_payload['news_list'] = news_list(request, 5)
    response_payload['banners'] = banners
    response_payload['left_nav_image'] = left_nav_image
    response_payload['initializer'] = initializer
    return render_to_response(
        template,
        response_payload,
        context_instance=RequestContext(request))
    
def current_classes(request, type, course=None, pages='5'):
    
    if course:
        class_list = Class.objects.filter(course=course, start_time__lt = datetime.now(), end_time__gt = datetime.now())
        sorted_target_list = None
        target = None
    else:
        class_list = current_class_list(request, None, type)
        target_list = []
        for item in class_list.all():
            if item.course.target not in target_list:
                target_list.append(item.course.target)
        sorted_target_list = sorted(target_list, key=lambda target: target.priority)
        
        target = request.GET.get('target')
        if target:
            class_list = current_class_list(request, target)
        else:
            try:
                target = target_list[0].pk
                class_list = current_class_list(request, target)
            except Exception:
                target = None
                class_list = None
                sys.exc_clear()
    
    # Determine the URL link to pass to template
    if type == TargetCategory.TESTPREPARATIONS:
        url = reverse('current_tp_classes')
    elif type == TargetCategory.LANGUAGEARTS:
        url = reverse('current_la_classes')
    else:
        url = reverse('current_classes')
    
    # Set pagination
    if class_list:
        list = Paginate(request, class_list, pages)
    else:
        list = None

    #return HttpResponse(sorted_target_list)
        
    return render_to_response(
        'courses/class_list.html',
        {
            'title': _('current classes'),
            'sub_nav': sorted_target_list,
            'class_list': list,
            'panel': '#currentclasses_panel',
            'url': url,
            'target': target,
            'none_message': get_message('no current schedules (short)'),
        },
        context_instance=RequestContext(request))
'''this is a necessary evil due to the original database design and to
keep the admin location selection simple
#get the localized location for each class
def add_localized_location(request, queryset):
    #loop through classes UGH
    for item in queryset:
        #loop through locations and get localized locations
        for locs in item.location.all():'''

def upcoming_classes(request, type, course=None, pages='5'):
    
    if course:
        class_list = Class.objects.filter(course=course, start_time__gt = datetime.now()).distinct()
        sorted_target_list = None
        target = None
    else:
        class_list = upcoming_class_list(request, None, type)
        target_list = []
        for item in class_list.all():
            if item.course.target not in target_list:
                target_list.append(item.course.target)
        sorted_target_list = sorted(target_list, key=lambda target: target.priority)
    
        target = request.GET.get('target')
        if target:
            class_list = upcoming_class_list(request, target)
        else:
            try:
                target = target_list[0].pk
                class_list = upcoming_class_list(request, target)
            except Exception:
                target = None
                class_list = None
                sys.exc_clear()
    
    # Determine the URL link to pass to template
    if type == TargetCategory.TESTPREPARATIONS:
        url = reverse('upcoming_tp_classes')
    elif type == TargetCategory.LANGUAGEARTS:
        url = reverse('upcoming_la_classes')
    else:
        url = reverse('upcoming_classes')
    
    # Set pagination
    if class_list:
        list = Paginate(request, class_list, pages)
    else:
        list = None
        
    return render_to_response(
        'courses/class_list.html',
        {
            'title': _('upcoming classes'),
            'sub_nav': sorted_target_list,
            'class_list': list,
            'panel': '#upcomingclasses_panel',
            'url': url,
            'target': target,
            'none_message': get_message('no upcoming schedules (short)'),
        },
        context_instance=RequestContext(request))
    
def class_preview(request, type=None, pages='3'):
    
    if type == TargetCategory.TESTPREPARATIONS:
        title = _('test preparation')
        url = reverse('testprep_schedule')
    elif type == TargetCategory.LANGUAGEARTS:
        title = _('language arts')
        url = reverse('languagearts_schedule')
    else:
        url = reverse('upcoming_classes')
    
    # Set pagination
    list = Paginate(request, recent_class_list(request, None, type), pages)
        
    return render_to_response(
        'courses/class_list_preview.html',
        {
            'title': title,
            'class_list': list,
            'panel': '#upcomingclasses_panel',
            'url': url,
        },
        context_instance=RequestContext(request))
        
    
def navigation(request, type=None, area='course'):
    
    # Get the client language from the session
    language = Language.get_language(request)
    category_type = type
    if category_type == 7:
        admissions_nav = True
        category_type = 1
    
    #course_queryset = Course.objects.filter(category=type, data_state=DataState.PUBLISHED)
    if category_type:
        if type == 7:
            targets = Target.objects.filter(category=category_type, data_state=DataState.PUBLISHED, course__name="Admissions Counseling") #TODO fix this to use database instead of string
        else:
            targets = Target.objects.filter(category=category_type, data_state=DataState.PUBLISHED)
    else:
        targets = Target.objects.filter(data_state=DataState.PUBLISHED)
    
    if area=='course':
        if type == TargetCategory.LANGUAGEARTS:
            back_link = reverse('languagearts_home')
            template = 'courses/navigation_la.html'
        elif type == TargetCategory.TESTPREPARATIONS:
            back_link = reverse('testpreparations_home')
            template = 'courses/navigation_tp.html'
            for target in targets:
                target.courses = Course.objects.filter(target=target, data_state=DataState.PUBLISHED).exclude(name__iexact="Admissions Counseling")
        elif admissions_nav:
            back_link = reverse('admissionscounseling_home')
            template = 'courses/navigation_ac.html'
            for target in targets:
                target.courses = Course.objects.filter(target=target)
        elif type == TargetCategory.CURRICULUMCONSULTING:
            back_link = reverse('curriculumconsulting_home')
            template = 'courses/navigation.html'
    elif area=='schedule':
        if type == TargetCategory.LANGUAGEARTS:
            back_link = reverse('languagearts_schedule')
            template = 'courses/navigation_schedule_la.html'
        elif type == TargetCategory.TESTPREPARATIONS:
            back_link = reverse('testprep_schedule')
            template = 'courses/navigation_schedule_tp.html'
            for target in targets:
                target.courses = Course.objects.filter(target=target, data_state=DataState.PUBLISHED)
        
    return render_to_response(
        template,
        {
            'target_list': targets,
            'back_link': back_link,
        },
        context_instance=RequestContext(request))

# OBSOLETE
def course_details(request, identifier):
    
    # Get the client language from the session
    language = Language.get_language(request)
    
    if language.pk != Language.DEFAULT:  # If a non-default language is requested, retrieve pages in that language.
        try:
            item = LocalizedCourse.objects.get(meta=identifier, language=language)
        except:
            try:
                item = LocalizedCourse.objects.get(meta=identifier, language=Language.DEFAULT)
            except:
                item = Course.objects.get(pk=identifier)
    else:
        try:
            item = LocalizedCourse.objects.get(meta=identifier, language=Language.DEFAULT)
        except:
            item = Course.objects.get(pk=identifier)
    
    # Convert the skill list into an array.
    if hasattr(item, 'meta'):
        item.weblinks = link_list(request, item.meta.pk)
        if item.skills:
            item.skill_list = item.skills.split(',')
    else:
        item.weblinks = link_list(request, item.pk)
    
    related_links = link_list(request, identifier)
    current_list = current_class_list(request, identifier)
    upcoming_list = upcoming_class_list(request, identifier)
        
    return render_to_response(
        'courses/course_details.html',
        {'course': item,
         'current_classes': current_list,
         'upcoming_classes': upcoming_list,
         'link_list': related_links,
         },
        context_instance=RequestContext(request))
    
def target_details(request, identifier):
    
    # Get the client language from the session
    language = Language.get_language(request)
    
    # TARGET SECTION
    # Get the localized target in the requested language, otherwise return the default language, otherwise return the meta data.
    if language.pk != Language.DEFAULT:  # If a non-default language is requested, retrieve pages in that language.
        try:
            target = LocalizedTarget.objects.get(meta=identifier, language=language)
        except:
            try:
                target = LocalizedTarget.objects.get(meta=identifier, language=Language.DEFAULT)
            except:
                target = Target.objects.get(pk=identifier)
    else:
        try:
            target = LocalizedTarget.objects.get(meta=identifier, language=Language.DEFAULT)
        except:
            target = Target.objects.get(pk=identifier)
    
    # COURSE SECTION  
    meta_queryset = Course.objects.filter(target=identifier, data_state=DataState.PUBLISHED)
    queryset = LocalizedCourse.objects.filter(meta__target=identifier, language=language, data_state=DataState.PUBLISHED)
    new_queryset = LocalSet(request, meta_queryset, queryset)
    
    for item in new_queryset:
        if hasattr(item, 'meta'):
            item.weblinks = link_list(request, item.meta.pk)
            if item.skills:
                item.skill_list = item.skills.split(',')
        else:
            item.weblinks = link_list(request, item.pk)
    
    return render_to_response(
        'courses/target_details.html',
        {
         'target': target,
         'courses': new_queryset,
        },
        context_instance=RequestContext(request))

def schedule(request, type):  # This is the index page of the schedule section
    
    if type == TargetCategory.TESTPREPARATIONS:
        template = 'courses/schedule_tp.html'
        banners = getBanners(request, BannerCategory.TP_SCHEDULE)
    elif type == TargetCategory.LANGUAGEARTS:
        template = 'courses/schedule_la.html'
        banners = getBanners(request, BannerCategory.LA_SCHEDULE)
        
    else:
        template = 'courses/schedule.html'
    
    recent_news = news_list(request, 5)
    print recent_news
    recent_blogs = blog_list(request, 5)
        
    return render_to_response(
        template,
        {'banners': banners,
         'news_list': recent_news,
         'blog_list': recent_blogs,
         },
        context_instance=RequestContext(request))
    
def class_list(request, target=None, course=None):
    if course:
        current_queryset = Class.objects.filter(course = course, start_time__lt = timezone.now(), end_time__gt = timezone.now()).distinct().order_by('start_time')
        upcoming_queryset = Class.objects.filter(course = course, start_time__gt = timezone.now()).distinct().order_by('start_time')
    else:
        current_queryset = Class.objects.filter(course__target = target, start_time__lt = timezone.now(), end_time__gt = timezone.now()).distinct().order_by('start_time')
        upcoming_queryset = Class.objects.filter(course__target = target, start_time__gt = timezone.now()).distinct().order_by('start_time')
    
    return render_to_response(
        'courses/schedule_list.html',
        {
         'current_class_list': current_queryset,
         'upcoming_class_list': upcoming_queryset,
         'none_message1': get_message('no upcoming schedules (long)'),
         'none_message2': get_message('no current schedules (long)'),
        },
        context_instance=RequestContext(request)
    )
    
def link_list(request, identifier):
    
    queryset = Weblink.objects.filter(courses = identifier).values()
    
    return queryset
    
def current_class_list(request, target=None, category=None):
    
    if target:
        queryset = Class.objects.filter(course__target = target, start_time__lt = datetime.now(), end_time__gt = datetime.now()).distinct().order_by('start_time')
    elif category: 
        queryset = Class.objects.filter(course__target__category = category, start_time__lt = datetime.now(), end_time__gt = datetime.now()).distinct().order_by('start_time')
    else:
        queryset = Class.objects.filter(start_time__lt = datetime.now(), end_time__gt = datetime.now()).distinct().order_by('start_time')
    
    return queryset

def upcoming_class_list(request, target=None, category=None):
    if target:
        queryset = Class.objects.filter(course__target = target, start_time__gt = datetime.now()).distinct().order_by('start_time')
    elif category:
        queryset = Class.objects.filter(course__target__category = category, start_time__gt = datetime.now()).distinct().order_by('start_time')
    else:
        queryset = Class.objects.filter(start_time__gt = datetime.now()).distinct().order_by('start_time')
    
    return queryset
    
def recent_class_list(request, target=None, category=None):
    
    if target:
        queryset = Class.objects.filter(course__target = target, end_time__gt = datetime.now()).order_by('-start_time')
    elif category: 
        queryset = Class.objects.filter(course__target__category = category, end_time__gt = datetime.now()).order_by('-start_time')
    else:
        queryset = Class.objects.filter(end_time__gt = datetime.now())
    
    return queryset

def course_link_list(request, identifier):
    
    queryset = Weblink.objects.filter(courses=identifier).values()
    
    return render_to_response(
        'panel_links.html',
        {
         'link_list': queryset,
        },
        context_instance=RequestContext(request))

def target_link_list(request, identifier):
    
    queryset = Weblink.objects.filter(courses__target=identifier).distinct().values()
    
    return render_to_response(
        'panel_links.html',
        {
         'link_list': queryset,
        },
        context_instance=RequestContext(request))
    
