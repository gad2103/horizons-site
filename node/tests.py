from django.core.urlresolvers import reverse

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_urls(self):
        # Test core urls
        test_url(self, '/')
        test_url(self, '/admin/')
        test_url(self, '/robots.txt')
        
        #Test basic pages
        test_url_from_name(self, 'instructor_home', code=301)
        #test_url_from_name(self, 'course_home', code=301)
        test_url_from_name(self, 'location_home')
        
###################################################################################################
# Convenience methods #############################################################################
###################################################################################################
        
def test_url(self, direction, *args, **kwargs):
    """ Test for the presence of a URL. """
    
    if 'code' in kwargs:
        code = kwargs['code']
    else:
        code = 200
    
    response = self.client.get(direction)
    
    try:
        self.assertEqual(response.status_code, code)
    except AssertionError, e:
        self.assertEqual(str(e), "Response didn't redirect as expected.")
        
# This command verifies whether a named url returns the expected response.
# Input: the only required parameter is the url.  By default it will check for response code 200.
# If you specify "code", it will check that that code is returned.
# You can also pass this command an instance of fighter, fightcard, venue, etc.,
# and it will perform some checks that the content details page is correct.
def test_url_from_name(self, direction, *args, **kwargs):
    """ Test for the presence of a URL name. """
    
    # Get the HTTP response code if provided.
    if 'code' in kwargs:
        code = kwargs['code']
    else:
        code = 200
    
    # Get some content to validate the returned page.
    if 'content' in kwargs:
        content = kwargs['content']
        response = self.client.get(reverse(direction, args=(content.pk,)))
    else:
        content = None
        response = self.client.get(reverse(direction))
    
    if content:
        pass
    else:
        try:
            self.assertEqual(response.status_code, code)
        except AssertionError, e:
            self.assertEqual(str(e), "Response didn't redirect as expected.")