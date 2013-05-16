from django.shortcuts import get_object_or_404, render_to_response, render, HttpResponse
from django.template import RequestContext

def home(request):
	page_title  = "Fundaci&oacute;n que Transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Bienvenidos a Fundaci&oacute;n que Transforma"
	menu_inicio = "current"
	section 	= "inicio"
	return render_to_response('sections/inicio.html', locals())
def nosotros(request):
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Nosotros"
	menu_inicio = "current"
	section 	= "nosotros"
	return render_to_response('sections/nosotros.html', locals())
def programas(request):
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Programas"
	menu_inicio = "current"
	section 	= "programas"
	return render_to_response('sections/programas.html', locals())
def ecotips(request):
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Ecotips"
	menu_inicio = "current"
	section 	= "ecotips"
	return render_to_response('sections/ecotips.html', locals())
def transparencia(request):
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Transparencia"
	menu_inicio = "current"
	section 	= "transparencia"
	return render_to_response('sections/transparencia.html', locals())
def talleristas(request):
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Talleristas"
	menu_inicio = "current"
	section 	= "talleristas"
	return render_to_response('sections/talleristas.html', locals())
def inversiones_sociales(request):
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Inversiones Sociales"
	menu_inicio = "current"
	section 	= "inversiones_sociales"
	return render_to_response('sections/inversiones_sociales.html', locals())
def contacto(request):
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Contacto"
	menu_inicio = "current"
	section 	= "contacto"
	return render_to_response('sections/contacto.html', locals())