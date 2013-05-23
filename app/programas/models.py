# -*- coding: utf-8 -*-

from django.db import models
from tinymce.models import HTMLField
from django.core.urlresolvers import reverse 
import datetime



class Program(models.Model):
	title = models.CharField(max_length=120)
	description = HTMLField()
	weight = models.IntegerField(blank=True, null=True)
	has_contact_form = models.BooleanField(default=False)
	contact_form_title = models.CharField('Contact form title', max_length=120, blank=True, null=True)
	reg_date = models.DateTimeField('Registration date', default=datetime.datetime.now)


class Image(models.Model):
	alt = models.CharField(max_length=140, blank=True, null=True)
	image = models.ImageField(upload_to='programas')
	is_cover = models.BooleanField(default=False)	
	weight = models.IntegerField(blank=True, null=True)
	program = models.ForeignKey(Program)

	class Meta:		
		ordering = ['weight']
		verbose_name_plural = 'Imagenes'
		verbose_name = 'Imagen'

	def __unicode__(self):
		return self.image.name