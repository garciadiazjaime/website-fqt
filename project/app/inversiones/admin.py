# -*- coding: utf-8 -*-

from django.contrib import admin

from app.inversiones.models import Toner, Logos


class LogosAdmin(admin.ModelAdmin):
	search_fields = ['alt']
	list_display = ('alt', 'image', 'weight', 'reg_date')
	list_filter = ['category', 'reg_date']	

admin.site.register(Logos, LogosAdmin)
admin.site.register(Toner)

