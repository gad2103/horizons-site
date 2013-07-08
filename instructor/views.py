from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

from banner.models import BannerCategory
from instructor.models import Instructor, LocalizedInstructor
from course.models import Target, TargetCategory, Course, LocalizedCourse
from newhorizons.views import news_list, blog_list, getBanners
from node.models import DataState, Language
from node.views import Paginate, LocalSet
from sitemessage.views import get_message
    
def index(request, type=None):
    
    if type == TargetCategory.TESTPREPARATIONS:
        template = 'instructors/index_tp.html'
        banners = getBanners(request, BannerCategory.TP_INSTRUCTORS)
        try:
            left_nav_image = SiteImage.objects.get(category=SiteImageCategory.TP_INSTRUCTORS)
        except Exception:
            left_nav_image = None
    elif type == TargetCategory.LANGUAGEARTS:
        template = 'instructors/index_la.html'
        banners = getBanners(request, BannerCategory.LA_INSTRUCTORS)
        try:
            left_nav_image = SiteImage.objects.get(category=SiteImageCategory.LA_INSTRUCTORS)
        except Exception:
            left_nav_image = None
    else:
        template = 'instructors/index.html'
        new_banners = None
    
    recent_news = news_list(request, 5)
    recent_blogs = blog_list(request, 5)
        
    return render_to_response(
        template,
        {'banners': banners,
         'left_nav_image': left_nav_image,
         'news_list': recent_news,
         'blog_list': recent_blogs,
         },
        context_instance=RequestContext(request))

def navigation(request, type=None, identifier=None):
    
    # Get the client language from the session
    language = Language.get_language(request)
    
    #course_queryset = Course.objects.filter(category=type, data_state=DataState.PUBLISHED)
    if type:
        targets = Target.objects.filter(category=type, data_state=DataState.PUBLISHED)
    else:
        targets = Target.objects.filter(data_state=DataState.PUBLISHED)
    
    if type == TargetCategory.LANGUAGEARTS:
        template = 'instructors/navigation_la.html'
        back_link = reverse('la_home_instructors')
    elif type == TargetCategory.TESTPREPARATIONS:
        template = 'instructors/navigation_tp.html'
        back_link = reverse('tp_home_instructors')
        for target in targets:
            target.courses = Course.objects.filter(target=target, data_state=DataState.PUBLISHED)
    else:
        template = 'instructors/navigation.html'
        back_link = reverse('instructor_home')
        
    return render_to_response(
        template,
        {'target_list': targets,
         #'expand': target,
         #'course_list': courses,
         'back_link': back_link,
         },
        context_instance=RequestContext(request))
    
def list(request, type):
    meta_queryset = Instructor.objects.filter(topics__target__category=type, data_state=DataState.PUBLISHED).distinct()
    queryset = LocalizedInstructor.objects.filter(meta__topics__target__category=type, data_state=DataState.PUBLISHED).distinct()
    new_queryset = LocalSet(request, meta_queryset, queryset)
    
    list = Paginate(request, new_queryset, 3)
    if type == TargetCategory.TESTPREPARATIONS:
        url = reverse('tp_instructor_list')
    elif type == TargetCategory.LANGUAGEARTS:
        url = reverse('la_instructor_list')
    
    return render_to_response(
        'instructors/details.html',
        {
            'details_list': list,
            'url': url,
        },
        context_instance=RequestContext(request)
    )

# The details view filters Instructor according to a Target selected.  The target pk is passed as 'identifier'.
def details(request, type=None, target=None, course=None):
        
    if course:
        meta_queryset = Instructor.objects.filter(topics=course, data_state=DataState.PUBLISHED).distinct()
        queryset = LocalizedInstructor.objects.filter(meta__topics=course, data_state=DataState.PUBLISHED)
    else:
        meta_queryset = Instructor.objects.filter(topics__target_id=target, data_state=DataState.PUBLISHED).distinct()
        queryset = LocalizedInstructor.objects.filter(meta__topics__target__id=target, data_state=DataState.PUBLISHED)
    
    new_queryset = LocalSet(request, meta_queryset, queryset)
        
    if course or target:
        if course:
            the_category = Course.objects.get(pk=course).target.category
            url = reverse('instructor_details', kwargs={'target': target, 'course': course})
        elif target:
            the_category = Target.objects.get(pk=target).category
            url = reverse('instructor_details', kwargs={'target': target})
            
        for instructor in new_queryset:
            instructor.topic_list = []
            if hasattr(instructor, 'meta'):
                for course in instructor.meta.topics.all():
                    if course.target.category == the_category:
                        instructor.topic_list.append(course)
            else:
                for course in instructor.topics.all():
                    if course.target.category == the_category:
                        instructor.topic_list.append(course)
    
    # Get the "none_message".
    if type:
        if type == TargetCategory.TESTPREPARATIONS:
            none_message = get_message('no tp instructor')
        elif type == TargetCategory.LANGUAGEARTS:
            none_message = get_message('no la instructor')
        else:
            none_message = get_message('');
    elif target:
        type = Target.objects.get(pk=target).category.pk 
        if type == TargetCategory.TESTPREPARATIONS:
            none_message = get_message('no tp instructor')
        elif type == TargetCategory.LANGUAGEARTS:
            none_message = get_message('no la instructor')
        else:
            none_message = get_message('');   
    else:
        none_message = get_message('');
    
    # Set up pagination
    list = Paginate(request, new_queryset, 3)
    
    return render_to_response(
        'instructors/details.html',
        {
            'details_list': list,
            'course_id': target,
            'none_message': none_message,
            'url': url,
        },
        context_instance=RequestContext(request))
