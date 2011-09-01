# -*- encoding: utf-8 -*-
from django.test import TestCase
from subscription.forms import SubscriptionForm

class TestSubscriptionForm(TestCase):
    def test_form_has_not_paid_field(self):
        form = SubscriptionForm()

        self.assertFalse(form.fields.get('paid'))

    def test_form_has_not_create_at_field(self):
        form = SubscriptionForm()

        self.assertFalse(form.fields.get('created_at'))

    def test_form_success_with_all_data(self):
        form = SubscriptionForm({
            'name': 'Joao Paulo Dubas',
            'cpf': '12345678901',
            'email': 'joao.dubas@gmail.com',
            'phone': ['11', '12345678']
        })

        self.assertTrue(form.is_valid())
    
    def test_form_error_when_cpf_has_less_than_11_digits(self):
        form = SubscriptionForm({
            'name': 'Joao Paulo Dubas',
            'cpf': '123456789',
            'email': 'joao.dubas@gmail.com',
            'phone': ['11', '12345678']
        })

        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors.has_key('cpf'))

    def test_form_error_when_cpf_has_alfa_numeric_character(self):
        form = SubscriptionForm({
            'name': 'Joao Paulo Dubas',
            'cpf': '1234567891a',
            'email': 'joao.dubas@gmail.com',
            'phone': ['11', '12345678']
        })

        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors.has_key('cpf'))

    def test_form__error_when_cpf_has_the_same_digits(self):
        form = SubscriptionForm({
            'name': 'Joao Paulo Dubas',
            'cpf': '11111111111',
            'email': 'joao.dubas@gmail.com',
            'phone': ['11', '12345678']
        })

        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors.has_key('cpf'))

    def test_form_must_have_phone_or_email(self):
        form = SubscriptionForm({
            'name': 'Joao Paulo Dubas',
            'cpf': '12345678901',
        })

        self.assertFalse(form.is_valid())
        self.assertTrue(form.non_field_errors())
