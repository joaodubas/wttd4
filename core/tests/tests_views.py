# -*- encoding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from core.models import Speaker

class SpeakerTest(TestCase):
    def setUp(self):
        Speaker.objects.create(
            name='Joao Paulo Dubas', \
            url='http://www.dbsdev.com.br/'
        )

    def test_view_list_speakers(self):
        response = self.client.get(reverse('list_speaker'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/list_speaker.html')
        self.assertTrue('show_all_info' in response.context)
        self.assertFalse(response.context['show_all_info'])
    
    def test_view_detail_about_speaker(self):
        response = self.client.get(reverse('detail_speaker', kwargs={'pk': 1, 'slug': 'joao-paulo-dubas'}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/detail_speaker.html')
        self.assertTrue('show_all_info' in response.context)
        self.assertTrue(response.context['show_all_info'])
    
    def test_try_to_see_a_speaker_that_dont_exist(self):
        response_1 = self.client.get(reverse('detail_speaker', kwargs={'pk': 1, 'slug': 'joao-paulo-dubas1'}))

        self.assertEqual(response_1.status_code, 404)

        response_2 = self.client.get(reverse('detail_speaker', kwargs={'pk': 2, 'slug': 'joao-paulo-dubas'}))

        self.assertEqual(response_2.status_code, 404)

