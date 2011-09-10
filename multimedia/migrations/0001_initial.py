# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Media'
        db.create_table('multimedia_media', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('talk', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Talk'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('media_id', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('multimedia', ['Media'])


    def backwards(self, orm):
        
        # Deleting model 'Media'
        db.delete_table('multimedia_media')


    models = {
        'core.speaker': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Speaker'},
            'avatar': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'core.talk': {
            'Meta': {'ordering': "('start_time', 'title')", 'object_name': 'Talk'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Speaker']", 'symmetrical': 'False'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'multimedia.media': {
            'Meta': {'object_name': 'Media'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media_id': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'talk': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Talk']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['multimedia']
