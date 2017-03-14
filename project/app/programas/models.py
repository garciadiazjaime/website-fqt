# -*- coding: utf-8 -*-

from django.db import models
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse 
import datetime
from django import forms
#from datetime import date

class ProgramManager(models.Manager):
	def get_programs(self):
		programs = Program.objects.all().order_by('-weight', '-reg_date')			
		data = []
		if len(programs) > 0:
			for row in programs:
				images = Image.objects.filter(program_id=row.id).order_by('weight')
				data.append({
					'info': row,
					'images': images,
					})
		return data

	def get_list_programs(self):
		programs = Program.objects.all().order_by('-weight', '-reg_date')			
		data = []
		if len(programs) > 0:
			for row in programs:				
				data.append({
					'title': row.title,					
					})
		return data


class Program(models.Model):
	WHERE_CHOICES = (
		(1, 'izquierda'),
		(2, 'derecha'),		
	)
	title = models.CharField(max_length=120)
	description_left = HTMLField(blank=True, null=True)
	description_right = HTMLField(blank=True, null=True)
	weight = models.IntegerField(blank=True, null=True)
	has_contact_form = models.BooleanField(default=False)
	contact_form_title = models.CharField('Contact form title', max_length=120, blank=True, null=True)
	reg_date = models.DateTimeField('Registration date', default=datetime.datetime.now)
	where_gallery = models.IntegerField(choices=WHERE_CHOICES, max_length=140)

	objects = models.Manager()
	objects_a = ProgramManager()

	class Meta:
		verbose_name = "Programa"
		verbose_name_plural = "Programas"

class Image(models.Model):
	alt = models.CharField(max_length=140, blank=True, null=True)
	image = models.FileField(upload_to='programas')	
	weight = models.IntegerField(blank=True, null=True)
	program = models.ForeignKey(Program)

	class Meta:		
		ordering = ['weight']
		verbose_name_plural = 'Imagenes'
		verbose_name = 'Imagen'

	def __unicode__(self):
		return self.image.name

class Talleristas(models.Model):
	CHOICES = (
			('Forestaciones / Huertos Escolares', 'Forestaciones / Huertos Escolares'), 
			('Talleres', 'Talleres'),
			('Eventos', 'Eventos'),
			('Actividades Operativas', 'Actividades Operativas'),
			('Experiencia Profesional', 'Experiencia Profesional'),
	)
	nombre = models.CharField(max_length=140)
	edad = models.CharField(max_length=140)
	email = models.EmailField(max_length=140)
	ocupacion = models.CharField(max_length=140)
	select_apoyo = models.CharField(choices=CHOICES,  max_length=140)	
	mensaje = models.CharField(max_length=500)
	ficha = models.FileField(upload_to='talleristas/%Y/%m')	
	reg_date = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return self.nombre

class TalleristasForm(forms.Form):
	CHOICES = (
			('Forestaciones / Huertos Escolares', 'Forestaciones / Huertos Escolares'), 
			('Talleres', 'Talleres'),
			('Eventos', 'Eventos'),
			('Actividades Operativas', 'Actividades Operativas'),
			('Experiencia Profesional', 'Experiencia Profesional'),
	)
	nombre = forms.CharField()
	edad = forms.CharField(max_length=140)
	email = forms.EmailField(max_length=140)
	ocupacion = forms.CharField(max_length=140)
	select_apoyo = forms.ChoiceField(choices=CHOICES)	
	mensaje = forms.CharField(widget=forms.Textarea)
	ficha = forms.FileField()

	def __init__(self, *args, **kwargs):
		super(TalleristasForm, self).__init__(*args, **kwargs)
		for row in ['nombre', 'edad', 'email', 'ocupacion']:
			self.fields[row].widget.attrs.update({'class' : 'custom_textbox required'})
		
		self.fields['select_apoyo'].widget.attrs.update({'class' : 'mySelectBoxClass'})
		self.fields['mensaje'].widget.attrs.update({'rows' : '5'})
		self.fields['ficha'].widget.attrs.update({'id' : 'BrowserHidden', 'onchange':"getElementById('FileField').value = getElementById('BrowserHidden').value;"})





