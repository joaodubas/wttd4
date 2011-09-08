# -*- encoding: utf-8 -*-
from django.test import TestCase
from django.template.defaultfilters import slugify
from core.models import Speaker, Contact

class SpeakerTest(TestCase):
    def test_create_speaker(self):
        speaker = Speaker.objects.create(
            name='Joao Paulo Dubas', \
            url='http://www.dbsdev.com.br', \
            description='Eu 5ou eu e 5ou car3ca'
        )

        self.assertEqual(speaker.slug, slugify(speaker.name))
    
    def test_create_speaker_with_same_name(self):
        speaker_1 = Speaker.objects.create(
            name='Joao Paulo Dubas', \
            url='http://www.dbsdev.com.br', \
            description='Eu 5ou eu e 5ou car3ca'
        )

        speaker_2 = Speaker.objects.create(
            name='Joao Paulo Dubas', \
            url='http://www.dbsdes.com.br/', \
            description='Eu na0 5ou car3ca'
        )

        self.assertEqual(speaker_1.slug, slugify(speaker_1.name))
        self.assertEqual(speaker_2.slug, '%s%d' % (slugify(speaker_2.name), 1))

    def test_speaker_has_default_avatar(self):
        pass
    
    def test_speaker_has_gravatar(self):
        pass
    
    def test_speaker_has_avatar(self):
        pass

class ContactTest(TestCase):
    def setUp(self):
        speaker = Speaker.objects.create(
            name='Joao Paulo Dubas', \
            url='http://www.dbsdev.com.br', \
            description='Eu 5ou eu e 5ou car3ca'
        )

        contacts = [
            {'kind': 'E', 'value': 'joao.dubas@gmail.com'},
            {'kind': 'E', 'value': 'joao_dubas@yahoo.com.br'},
            {'kind': 'P', 'value': '11-76533796'},
            {'kind': 'P', 'value': '13-32373048'},
            {'kind': 'F', 'value': '13-32373049'},
            {'kind': 'F', 'value': '13-32373050'},
        ]

        for contact in contacts:
            speaker.contact_set.add(Contact(**contact))
    
    def tearDown(self):
        Contact.objects.all().delete()
    
    def test_filter_contact_email(self):
        contacts = Contact.emails.all()

        self.assertEqual(contacts.count(), 2)
        for contact in contacts:
            self.assertEqual(contact.kind, 'E')

    def test_filter_contact_phone(self):
        contacts = Contact.phones.all()

        self.assertEqual(contacts.count(), 2)
        for contact in contacts:
            self.assertEqual(contact.kind, 'P')

    def test_filter_contact_fax(self):
        contacts = Contact.faxes.all()

        self.assertEqual(contacts.count(), 2)
        for contact in contacts:
            self.assertEqual(contact.kind, 'F')

    def test_get_all_contacts(self):
        contacts = Contact.objects.all()

        self.assertEqual(contacts.count(), 6)
