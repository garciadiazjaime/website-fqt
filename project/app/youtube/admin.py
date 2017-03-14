# -*- coding: utf-8 -*-

from django.contrib import admin

from app.youtube.models import Ecocapsulas, Categoria

class CategoriaAdmin(admin.ModelAdmin):
	search_fields = ['name', 'url', 'slug', 'weight']
	list_display = ('name', 'url', 'weight')

class EcocapsulasAdmin(admin.ModelAdmin):
	search_fields = ['title',]
	list_display = ('title', 'status', 'reg_date')
	list_filter = ['status', 'reg_date']	

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Ecocapsulas, EcocapsulasAdmin)

