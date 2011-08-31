# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Subscription.phone'
        db.alter_column('subscription_subscription', 'phone', self.gf('django.db.models.fields.CharField')(max_length=11))


    def backwards(self, orm):
        
        # Changing field 'Subscription.phone'
        db.alter_column('subscription_subscription', 'phone', self.gf('django.db.models.fields.CharField')(max_length=10))


    models = {
        'subscription.subscription': {
            'Meta': {'ordering': "('-created_at',)", 'object_name': 'Subscription'},
            'cpf': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '11'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'})
        }
    }

    complete_apps = ['subscription']
