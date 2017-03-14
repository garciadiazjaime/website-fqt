# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Program'
        db.create_table('programas_program', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('description_left', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('description_right', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('has_contact_form', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('contact_form_title', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('reg_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('where_gallery', self.gf('django.db.models.fields.IntegerField')(max_length=140)),
        ))
        db.send_create_signal('programas', ['Program'])

        # Adding model 'Image'
        db.create_table('programas_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alt', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programas.Program'])),
        ))
        db.send_create_signal('programas', ['Image'])

        # Adding model 'Talleristas'
        db.create_table('programas_talleristas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('edad', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=140)),
            ('ocupacion', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('select_apoyo', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('mensaje', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('ficha', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('reg_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('programas', ['Talleristas'])


    def backwards(self, orm):
        # Deleting model 'Program'
        db.delete_table('programas_program')

        # Deleting model 'Image'
        db.delete_table('programas_image')

        # Deleting model 'Talleristas'
        db.delete_table('programas_talleristas')


    models = {
        'programas.image': {
            'Meta': {'ordering': "['weight']", 'object_name': 'Image'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programas.Program']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'programas.program': {
            'Meta': {'object_name': 'Program'},
            'contact_form_title': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'description_left': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'description_right': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'has_contact_form': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reg_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'where_gallery': ('django.db.models.fields.IntegerField', [], {'max_length': '140'})
        },
        'programas.talleristas': {
            'Meta': {'object_name': 'Talleristas'},
            'edad': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '140'}),
            'ficha': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mensaje': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'ocupacion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'reg_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'select_apoyo': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['programas']