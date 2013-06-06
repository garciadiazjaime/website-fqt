# -*- coding: utf-8 -*-

from django.db import models

class Infographic(models.Model):
	alt = models.CharField(max_length=140, blank=True, null=True)
	image = models.ImageField(upload_to='infographic')
	big_image = models.ImageField(upload_to='infographic')
	weight = models.IntegerField(blank=True, null=True)

	def __unicode__(self):
		return self.image.name

	class Meta:
		verbose_name = "Transparencia"
		verbose_name_plural = "Infográficos"
