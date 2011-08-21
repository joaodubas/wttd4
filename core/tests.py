from django.test import TestCase


class HomepageUrlTest(TestCase):
    def test_success_when_get_homepage(self):
        '''
        Verifies if the homepage is loaded and uses the specified template.
        '''
        response = self.client.get('/')
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'index.html')
