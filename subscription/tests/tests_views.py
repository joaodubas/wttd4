# -*- encoding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

class TestSubscriptionViews(TestCase):
    def test_new_subscription(self):
        response = self.client.get(reverse('subscription:subscribe'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'subscription/form.html')
    
    def test_send_subscription_with_all_data(self):
        form = {
            'name': 'Joao Paulo Dubas',
            'cpf': '12345678901',
            'email': 'joao.dubas@gmail.com',
            'phone': ['11','12345678']
        }
        response = self.client.post(reverse('subscription:subscribe'), form)

        self.assertRedirects(response, reverse('subscription:success', args=['1']))

    def test_send_subscription_without_email(self):
        form = {
            'name': 'Joao Paulo Dubas',
            'cpf': '12345678901',
            'phone': ['11','12345678']
        }
        response = self.client.post(reverse('subscription:subscribe'), form)

        self.assertRedirects(response, reverse('subscription:success', args=['1']))

    def test_send_subscription_without_phone(self):
        form = {
            'name': 'Joao Paulo Dubas',
            'cpf': '12345678901',
            'email': 'joao.dubas@gmail.com',
        }
        response = self.client.post(reverse('subscription:subscribe'), form)

        self.assertRedirects(response, reverse('subscription:success', args=['1']))

    
    def test_send_subscription_without_cpf(self):
        form = {
            'name': 'Joao Paulo Dubas',
            'email': 'joao.dubas@gmai.com',
            'phone': ['11', '12345678']
        }
        response = self.client.post(reverse('subscription:subscribe'), form)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'subscription/form.html')
        self.assertFormError(response, 'form', 'cpf', [_(u'This field is required.')])

    def test_send_subscription_with_cpf_that_has_the_same_digits(self):
        form = {
            'name': 'Joao Paulo Dubas',
            'cpf': '11111111111',
            'email': 'joao.dubas@gmail.com',
            'phone': ['11', '12345678']
        }
        response = self.client.post(reverse('subscription:subscribe'), form)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'subscription/form.html')
        self.assertFormError(response, 'form', 'cpf', [_(u'CPF inválido.')])
    
    def test_send_subscription_without_email_or_phone(self):
        form = {
            'name': 'Joao Paulo Dubas',
            'cpf': '12345678901',
        }
        response = self.client.post(reverse('subscription:subscribe'), form)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'subscription/form.html')
        self.assertFormError(response, 'form', None, [_(u'Informe o e-mail ou o telefone.')])
