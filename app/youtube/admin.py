# -*- coding: utf-8 -*-

from django.contrib import admin

from app.youtube.models import Video, Video_Category


class VideoAdmin(admin.ModelAdmin):
	search_fields = ['title', ]
	list_display = ('title', 'status', 'reg_date')
	list_filter = ['status', 'reg_date']	

admin.site.register(Video_Category)
admin.site.register(Video, VideoAdmin)

