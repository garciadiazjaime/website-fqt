from django.db import models
import datetime

class Categoria(models.Model):
	name = models.CharField(max_length=120)
	url = models.CharField(max_length=500)
	slug = models.CharField(max_length=500)
	weight = models.IntegerField(blank=True, null=True)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['-weight']

class Ecocapsulas(models.Model):
	title = models.CharField(max_length=120)
	video_id = models.CharField(max_length=45)
	source = models.CharField(max_length=255)
	status = models.BooleanField(default=True)
	weight = models.IntegerField(blank=True, null=True)
	reg_date = models.DateTimeField('Registration date', default=datetime.datetime.now)
	category = models.ForeignKey(Categoria)

	def __unicode__(self):
		return self.title
	