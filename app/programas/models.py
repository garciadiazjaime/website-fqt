# -*- coding: utf-8 -*-

from django.db import models
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse 
import datetime

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
