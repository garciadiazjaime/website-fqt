# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse 
import datetime


class Program(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	weight = models.IntegerField(blank=True, null=True)
	has_contact_form = models.BooleanField(default=False)	
	reg_date = models.DateTimeField('Fecha de registro', default=datetime.datetime.now)


class Image(models.Model):
	alt = models.CharField(max_length=140)
	url = models.FileField(upload_to='programas')
	is_cover = models.BooleanField(default=False)	
	weight = models.IntegerField(blank=True, null=True)
	program = models.ForeignKey(Program)
	class Meta:		
		ordering = ['weight']
		verbose_name_plural = 'Imagenes'
		verbose_name = 'Imagen'
	def __unicode__(self):
		return self.url.name
	#def get_absolute_url(self):
	#	return reverse('app.programas.views.show_category', args=(str(self.slug),))