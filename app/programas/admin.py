# -*- coding: utf-8 -*-

from django.contrib import admin

from app.programas.models import Program, Image

from django.contrib.auth.models import User, Group

#admin.site.unregister(User)
#admin.site.unregister(Group)


class ImageInline(admin.StackedInline):
	#fieldsets = [
	#	('Información', {'fields': ['alt', 'url']}),
	#	('Pertenece a:', {'fields': ['cover', 'instalaciones', 'logros', 'internacional', 'humana', 'deportiva']}),
	#]
	model = Image
	extra = 3

class ProgramAdmin(admin.ModelAdmin):
	inlines = [ImageInline]
	search_fields = ['title', 'description_left', 'description_right']
	list_display = ('title', 'description_left', 'description_right', 'has_contact_form', 'reg_date')
	list_filter = ['has_contact_form', 'reg_date']	

admin.site.register(Program, ProgramAdmin)

