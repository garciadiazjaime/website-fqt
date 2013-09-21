# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categoria'
        db.create_table('youtube_categoria', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cat_class', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
        ))
        db.send_create_signal('youtube', ['Categoria'])

        # Adding model 'Ecocapsulas'
        db.create_table('youtube_ecocapsulas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('video_id', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('reg_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['youtube.Categoria'])),
        ))
        db.send_create_signal('youtube', ['Ecocapsulas'])


    def backwards(self, orm):
        # Deleting model 'Categoria'
        db.delete_table('youtube_categoria')

        # Deleting model 'Ecocapsulas'
        db.delete_table('youtube_ecocapsulas')


    models = {
        'youtube.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'cat_class': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'youtube.ecocapsulas': {
            'Meta': {'object_name': 'Ecocapsulas'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['youtube.Categoria']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reg_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['youtube']