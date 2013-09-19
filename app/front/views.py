# -*- encoding: utf-8 -*-

from django.shortcuts import get_object_or_404, render_to_response, render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from app.front.menu import Menu
from app.programas.models import Program
from app.transparencia.models import Infographic
from app.downloads.models import Download
from app.inversiones.models import Toner
from app.youtube.models import Categoria, Ecocapsulas
from app.inversiones.models import Logos
from django.core.mail import send_mail
import re
import unidecode


from django.core.context_processors import csrf
import sys
from django.core.mail import EmailMultiAlternatives




menu = Menu()

def home(request):
	is_chrome = True if 'Chrome' in request.META['HTTP_USER_AGENT'] else False
	page_title  = "Fundaci&oacute;n que Transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Bienvenidos a Fundaci&oacute;n que Transforma"
	menu_inicio = "current"
	section 	= "inicio"
	main_menu = menu.get_main(section)
	footer_menu = menu.get_footer()

	return render_to_response('sections/inicio.html', locals())

def nosotros(request, category=''):
	is_chrome = True if 'Chrome' in request.META['HTTP_USER_AGENT'] else False
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Nosotros"
	menu_inicio = "current"
	section 	= "nosotros"
	main_menu = menu.get_main(section)
	footer_menu = menu.get_footer()

	return render_to_response('sections/nosotros.html', locals())

def programas(request, category=''):	
	is_chrome = True if 'Chrome' in request.META['HTTP_USER_AGENT'] else False
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
	data = Program.objects.all().order_by('-weight', '-reg_date')
	select = ''
	for row in data:
		if slugify(row.title) == form:
			select += '<option value="' + slugify(row.title) + '" selected>' + row.title + '</option>'
		else:
			select += '<option value="' + slugify(row.title) + '">' + row.title + '</option>'
	return render_to_response('sections/inscripcion.html', locals())

@csrf_exempt
def programa_inscribite(request):
	data = ''
	for key, value in request.POST.iteritems():
		data += key + ': ' + value + "\n"
	#send_mail('Programa Inscripción', data, 'info@fqt.com', ['info@fqt.com'])
	return HttpResponse('true')

def ecotips(request, category='', slug=''):
	is_chrome = True if 'Chrome' in request.META['HTTP_USER_AGENT'] else False
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Ecotips"
	menu_inicio = "current"
	section 	= "ecotips"
	main_menu = menu.get_main(section)
	footer_menu = menu.get_footer()
	categories = Categoria.objects.all().order_by('-weight')
	if slug != '':
		ecocapsulas = Ecocapsulas.objects.filter(category__slug=slug).order_by('-weight')
	else:
		ecocapsulas = Ecocapsulas.objects.all().order_by('-weight')

	return render_to_response('sections/ecotips.html', locals())

def transparencia(request, category=''):
	is_chrome = True if 'Chrome' in request.META['HTTP_USER_AGENT'] else False
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
	is_chrome = True if 'Chrome' in request.META['HTTP_USER_AGENT'] else False
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
	is_chrome = True if 'Chrome' in request.META['HTTP_USER_AGENT'] else False
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Campa&ntilde;as y donantes"
	menu_inicio = "current"
	section 	= "campanas_donantes"
	main_menu = menu.get_main(section)
	footer_menu = menu.get_footer()
	if Toner.objects.count():
		toner = Toner.objects.filter()[0]
		counter = toner.parse_to_span
	else:
	 	toner = ''
		counter = '<span>0</span>'
	toner = Logos.objects.filter(category=1).order_by('-weight', '-id')
	aliados = Logos.objects.filter(category=2).order_by('-weight', '-id')
	universidades = Logos.objects.filter(category=3).order_by('-weight', '-id')
	inversionistas = Logos.objects.filter(category=4).order_by('-weight', '-id')
	especie = Logos.objects.filter(category=5).order_by('-weight', '-id')

	return render_to_response('sections/inversiones_sociales.html', locals())

def contacto(request, category=''):
	is_chrome = True if 'Chrome' in request.META['HTTP_USER_AGENT'] else False
	page_title  = "Fundaci&oacute;n que transforma."
	keywords 	= "fundaci&oacute;n transforma"
	description = "Contacto"
	menu_inicio = "current"
	section 	= "contacto"
	main_menu = menu.get_main(section)
	footer_menu = menu.get_footer()

	return render_to_response('sections/contacto.html', locals())

def test(request):
	return HttpResponse('asfd')

def slugify(str):
    str = unidecode.unidecode(str).lower()
    return re.sub(r'\W+','-',str)

@csrf_exempt
def send_mail_form(request):
	c = {}
	c.update(csrf(request))
	if request.is_ajax():
		response = 'error'
		email_msg = ''
		name = request.POST.get('name', '')
		email = request.POST.get('email', '')
		message = request.POST.get('message', '')
		if name == '' or email == '' or message == '':
			response = 'empty_data'
		else:
			email_msg = """
				Name: <b>""" + str(name)  + """</b><br/>
				Email: <b>""" + str(email)  + """</b><br />
				Message: <b>""" + str(message)  + """</b><br />
			"""
			try:
				text_content = 'Mensaje enviado desde la forma de contacto'
				html_content = email_msg
				msg = EmailMultiAlternatives('Contact Form', text_content, email, ['contacto@fqt.org.mx ', 'info.mintitmedia@gmail.com',])
				msg.attach_alternative(html_content, "text/html")
				msg.send()
				response = "success"
			except:
				response = "Unexpected error:", sys.exc_info()
		return HttpResponse(response, c)
	else:
		return HttpResponse(status=400)