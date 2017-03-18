# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Toner'
        db.create_table('inversiones_toner', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('counter', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('inversiones', ['Toner'])

        # Adding model 'Logos'
        db.create_table('inversiones_logos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alt', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.IntegerField')(max_length=140)),
            ('reg_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('inversiones', ['Logos'])


    def backwards(self, orm):
        # Deleting model 'Toner'
        db.delete_table('inversiones_toner')

        # Deleting model 'Logos'
        db.delete_table('inversiones_logos')


    models = {
        'inversiones.logos': {
            'Meta': {'object_name': 'Logos'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.IntegerField', [], {'max_length': '140'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'reg_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'inversiones.toner': {
            'Meta': {'object_name': 'Toner'},
            'counter': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['inversiones']