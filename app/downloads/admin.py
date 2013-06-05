# -*- coding: utf-8 -*-

from django.contrib import admin

from app.downloads.models import Download


class DownloadAdmin(admin.ModelAdmin):
	search_fields = ['title']
	list_display = ('title', 'status', 'reg_date')
	list_filter = ['status', 'reg_date']	

admin.site.register(Download, DownloadAdmin)

