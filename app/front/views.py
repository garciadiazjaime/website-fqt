from django.shortcuts import get_object_or_404, render_to_response, render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from app.front.menu import Menu
from app.programas.models import Program
from app.transparencia.models import Infographic
from app.downloads.models import Download
from app.inversiones.models import Toner

menu = Menu()

def home(request):
	page_title  = "Fundaci&oacute;n que Transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Bienvenidos a Fundaci&oacute;n que Transforma"
	menu_inicio = "current"
	section 	= "inicio"
	main_menu = menu.get_main(section)
	footer_menu = menu.get_footer()

	return render_to_response('sections/inicio.html', locals())

def nosotros(request, category=''):
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Nosotros"
	menu_inicio = "current"
	section 	= "nosotros"
	main_menu = menu.get_main(section)
	footer_menu = menu.get_footer()

	return render_to_response('sections/nosotros.html', locals())

def programas(request, category=''):	
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Programas"
	menu_inicio = "current"
	section 	= "programas"
	main_menu = menu.get_main(section)
	list_programs = Program.objects_a.get_list_programs()
	programs = Program.objects_a.get_programs()
	footer_menu = menu.get_footer()

	return render_to_response('sections/programas.html', locals())

@csrf_exempt
def inscripcion(request, form=''):
	return HttpResponse('yea')
	#return render_to_response('sections/programas2.html', locals())

def ecotips(request, category=''):
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Ecotips"
	menu_inicio = "current"
	section 	= "ecotips"
	main_menu = menu.get_main(section)
	footer_menu = menu.get_footer()

	return render_to_response('sections/ecotips.html', locals())

def transparencia(request, category=''):
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Transparencia"
	menu_inicio = "current"
	section 	= "transparencia"
	main_menu = menu.get_main(section)
	footer_menu = menu.get_footer()
	infographic = Infographic.objects.all()

	return render_to_response('sections/transparencia.html', locals())

def talleristas(request, category=''):
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Talleristas"
	menu_inicio = "current"
	section 	= "talleristas"
	main_menu = menu.get_main(section)
	footer_menu = menu.get_footer()
	downloads = Download.objects.all()

	return render_to_response('sections/talleristas.html', locals())

def inversiones_sociales(request, category=''):
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Inversiones Sociales"
	menu_inicio = "current"
	section 	= "inversiones_sociales"
	main_menu = menu.get_main(section)
	footer_menu = menu.get_footer()
	toner = Toner.objects.filter()[0]
	counter = toner.parse_to_span()
	#return HttpResponse(counter)

	return render_to_response('sections/inversiones_sociales.html', locals())

def contacto(request, category=''):
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Contacto"
	menu_inicio = "current"
	section 	= "contacto"
	main_menu = menu.get_main(section)
	footer_menu = menu.get_footer()

	return render_to_response('sections/contacto.html', locals())