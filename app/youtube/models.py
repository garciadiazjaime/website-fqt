from django.db import models
import datetime

class Video_Category(models.Model):
	name = models.CharField(max_length=120)

	def __unicode__(self):
		return self.name

class Video(models.Model):
	title = models.CharField(max_length=120)
	source = models.URLField(max_length=255)
	status = models.BooleanField(default=True)
	reg_date = models.DateTimeField('Registration date', default=datetime.datetime.now)
	category = models.ForeignKey(Video_Category)

	def __unicode__(self):
		return self.title
