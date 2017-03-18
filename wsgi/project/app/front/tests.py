from django.shortcuts import get_object_or_404, render_to_response, render, HttpResponse
from apps.noticias.models import Gallery, Image
from django.template import RequestContext

def index(request):
	page_title  = "Instituto Bilingue Santillana del Mar."
	keywords 	= "escuela IBSM"
	description = "Educaci&oacute;n preescolar, primaria, secundaria y preparatoria"
	menu_inicio = "current"
	section 	= "inicio"
	mydata = Gallery.objects_a.get_last_galleries()[0:9]
	return render_to_response('sections/inicio.html', locals())