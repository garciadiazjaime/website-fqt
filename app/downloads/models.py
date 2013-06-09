# -*- coding: utf-8 -*-

from django.db import models
import datetime

class Download(models.Model):
	title = models.CharField(max_length=120)
	source = models.ImageField(upload_to='downloads')
	status = models.BooleanField(default=True)
	reg_date = models.DateTimeField('Registration date', default=datetime.datetime.now)

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = "Talleristas"
		verbose_name_plural = "Descargables"
