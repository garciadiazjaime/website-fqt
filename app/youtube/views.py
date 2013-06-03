from django.shortcuts import get_object_or_404, render_to_response, render, HttpResponse
import gdata.youtube
import gdata.youtube.service
from app.youtube.models import Categoria, Ecocapsulas
import re

def update_ecocapsulas(request):
	response = []
	yt_service = gdata.youtube.service.YouTubeService()
	#yt_service.ssl = True
	#yt_service.developer_key = 'AI39si7Z4KFJV64OT94jeyIQ6XT1j3JyltKuxJhxsevLvAr0LPp7cuc6brIoeJ74VxjuwTjzvw0Kw5mw5IK1zE1P74fn2BThhw'
	#yt_service.client_id = '917242802419.apps.googleusercontent.com'
	
	playlist_video_feed = yt_service.GetYouTubePlaylistFeed(username='FQTransforma')
	c = 0
	v = 0
	name = ''
	url = ''
	video = ''
	category_id = 0
	
	for playlist_video_entry in playlist_video_feed.entry:
		tmp = str(playlist_video_entry.id)
		tmp2 = tmp.split('/')
		url = tmp2[-2][:-1]
		flag = Categoria.objects.filter(url=url)
		if len(flag) == 0:
			name = re.sub('<[^<]+?>', '', str(playlist_video_entry.title))
			cat = Categoria(name=name, url=url)
			cat.save()
			category_id = cat.id
			c += 1
		else:
			category_id = flag[0].id
			url = flag[0].url
		playlist_uri = 'http://gdata.youtube.com/feeds/api/playlists/' + url
		playlist_channel_feed = yt_service.GetYouTubePlaylistVideoFeed(uri=playlist_uri)
		for row in playlist_channel_feed.entry:
			title = name = re.sub('<[^<]+?>', '', str(row.title))
			source = str(row.media.player.url)
			flag2 = Ecocapsulas.objects.filter(source=source)
			if len(flag2) == 0:
				eco = Ecocapsulas(title=title, source=source, category_id=category_id)
				eco.save()
				v += 1

	return HttpResponse('catetorias: ' + str(c) + ', videos: ' + str(v))