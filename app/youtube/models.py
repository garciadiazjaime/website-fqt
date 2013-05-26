from django.db import models
import datetime

class Categoria(models.Model):
	name = models.CharField(max_length=120)
	weight = models.IntegerField(blank=True, null=True)

	def __unicode__(self):
		return self.name

class Ecocapsulas(models.Model):
	title = models.CharField(max_length=120)
	source = models.URLField(max_length=255)
	status = models.BooleanField(default=True)
	weight = models.IntegerField(blank=True, null=True)
	reg_date = models.DateTimeField('Registration date', default=datetime.datetime.now)
	category = models.ForeignKey(Categoria)

	def __unicode__(self):
		return self.title
