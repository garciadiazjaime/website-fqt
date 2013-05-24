from django.db import models
import datetime

class Toner(models.Model):
	counter = models.IntegerField()

class Logos(models.Model):
	CATEGORY_CHOICES = (
		(1, 'toner'),
		(2, 'aliados'),
		(3, 'universidades'),
		(4, 'inversionistas'),
		(5, 'especie'),
	)
	alt = models.CharField(max_length=140, blank=True, null=True)
	image = models.ImageField(upload_to='inversiones')
	weight = models.IntegerField(blank=True, null=True)
	link = models.URLField(blank=True, null=True)
	category = models.CharField(choices=CATEGORY_CHOICES, max_length=140)
	reg_date = models.DateTimeField('Registration date', default=datetime.datetime.now)