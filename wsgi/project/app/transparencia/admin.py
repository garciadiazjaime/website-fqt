# -*- coding: utf-8 -*-

from django.contrib import admin

from app.transparencia.models import Infographic

class InfographicAdmin(admin.ModelAdmin):
	list_display = ( 'image', 'alt','weight')

admin.site.register(Infographic, InfographicAdmin)

