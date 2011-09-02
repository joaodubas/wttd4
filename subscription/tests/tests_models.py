# -*- encoding: utf-8 -*-
from django.test import TestCase
from django.core import mail
from django.core.exceptions import ValidationError
from datetime import date
from subscription.models import Subscription

class TestSubscriptionModel(TestCase):
    def test_save_subscription(self):
        subscriber = Subscription(
            name='Joao Paulo Dubas',
            cpf='12345678901',
            email='joao.dubas@gmail.com',
            phone='11-12345678'
        )

        subscriber.save()

        self.assertEqual(subscriber.pk, 1)
        self.assertEqual(subscriber.created_at.date(), date.today())
        self.assertFalse(subscriber.paid)
    
    def test_send_email_after_save_form(self):
        self.assertEqual(len(mail.outbox), 0)

        subscriber = Subscription(
            name='Joao Paulo Dubas',
            cpf='12345678901',
            email='joao.dubas@gmail.com',
            phone='11-12345678'
        )
        subscriber.save()

        self.assertEqual(len(mail.outbox), 1)

class TestSubscriptionModelIntegrity(TestCase):
    def setUp(self):
        subscriber = Subscription(
            name='Joao Paulo Dubas',
            cpf='12345678901',
            email='joao.dubas@gmail.com',
            phone='11-12345678'
        )

        subscriber.save()
    
    def tearDown(self):
        Subscription.objects.all().delete()

    def test_fail_to_save_repeated_cpf(self):
        subscriber = Subscription(
            name='Americo Paulo Dubas',
            cpf='12345678901',
            email='joao.dubas@gmail.com',
            phone='11-12345678'
        )

        self.assertRaises(ValidationError, subscriber.clean)

    def test_fail_to_save_repeated_email(self):
        subscriber = Subscription(
            name='Americo Paulo Dubas',
            cpf='98765432101',
            email='joao.dubas@gmail.com',
            phone='11-12345678'
        )

        self.assertRaises(ValidationError, subscriber.clean)
