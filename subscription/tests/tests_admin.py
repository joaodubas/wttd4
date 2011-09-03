# -*- encoding: utf-8 -*-
from django.test import TestCase
from django.contrib.auth.models import User
from subscription.models import Subscription

class TestSubscriptionAdmin(TestCase):
    models = [User, Subscription]

    def setUp(self):
        User.objects.create_superuser(username='joaoadubas', email='joao.dubas@gmail.com', password='dubas')

        subscriptions = [
            {
                'name': 'joao paulo dubas',
                'cpf': '12345678901',
                'email': 'joaodubas@gmail.com'
            },
            {
                'name': 'claudio eduardo dubas',
                'cpf': '12345678902',
                'email': 'claudiodubas@gmail.com'
            },
            {
                'name': 'americo antonio dubas',
                'cpf': '12345678903',
                'email': 'claudiodubas@gmail.com'
            },
            {
                'name': 'ana paula dubas',
                'cpf': '12345678904',
                'email': 'anadubas@gmail.com'
            },
            {
                'name': 'luiz fernando dubas',
                'cpf': '12345678905',
                'email': 'luizdubas@gmail.com'
            },
        ]

        for s in subscriptions:
            Subscription(**s).save()

    def tearDown(self):
        for m in self.models:
            m.objects.all().delete()

    def test_set_subscription_as_paid(self):
        pass
    
    def test_export_subscription_as_csv(self):
        pass