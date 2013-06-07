# -*- coding: utf-8 -*-

from django.utils.encoding import smart_str
from app.programas.models import Program
from app.youtube.models import Categoria
from slugify import slugify


class Menu(object):

	items = [			
			{				
				'href': 'inicio',
				'title': 'Inicio',				
			},
			{				
				'href': 'nosotros',
				'title': 'Nosotros',				
			},
			{				
				'href': 'programas',
				'title': 'Programas',
			},
			{				
				'href': 'ecotips',
				'title': 'Ecotips',
			},
			{				
				'href': 'transparencia',
				'title': 'Transparencia',				
			},
			{				
				'href': 'talleristas',
				'title': 'Talleristas',				
			},
			{				
				'href': 'campanas_donantes',
				'title': 'Campa&ntilde;as y donantes',
				'child':[
					{
						'href': 'campanas',
						'title': 'Campa&ntilde;as',
					},	
					{
						'href': 'tipos-donativos',
						'title': 'Tipos de donativos',
					},
					{
						'href': 'inversionistas-sociales',
						'title': 'Inversionistas Sociales',
					},
				],
			},			
			{				
				'href': 'contacto',
				'title': 'Contacto',
			},
		]


	def get_main(self, section):
		response = ''		
		child = ''
		for row in self.items:
			child = ''
			if row['href'] == 'programas':
				programas = Program.objects.all().order_by('-weight', '-reg_date')
				i = 0
				for row2 in programas:
					sublist_class=""
					if i == 0: sublist_class="first"
					child +=  "<li class=\""+sublist_class+"\" ><a title=\""+row2.title +"\" href=\"/"+row['href']+"/"+slugify(row2.title)+"\"><span>"+row2.title+"</span></a></li>"
					i += 1
			
			elif row['href'] == 'campanas_donantes' and 'child' in row:
				i = 0
				for row2 in row['child']:
					sublist_class=""
					if i == 0: sublist_class="first"
					child +=  "<li class=\""+sublist_class+"\"><a title=\""+row2['title']+"\" href=\"/"+row['href']+"/"+row2['href']+"\"><span>"+row2['title']+"</span></a></li>"
					i += 1

			if len(child):
				child = "<ul class=\"child\">" + child + "</ul>"

			if row['href'] == section:
				response += "<li class=\""+row['href']+" current \"><a title=\"/"+row['title'] +"\" href=\"/"+row['href']+"\"><span>"+row['title']+"</span></a> " + child + "</li>"
			else:
				response += "<li class=\""+row['href']+"\"><a title=\"/"+row['title'] +"\" href=\"/"+row['href']+"\"><span>"+row['title']+"</span></a> " + child + "</li>"

		if len(response):
			response = "<ul class=\"menu\">" + response + "</ul>"
		return response

	def get_footer(self):
		programs = []
		programs ={
			'programs': Program.objects_a.get_list_programs(),
			}
		return programs

	def get_child(self, section, data):
		response = ''
		for row in data:
			li_id = row['li_id'] if row.has_key('li_id') else ''						
			response += "<li id=\""+ li_id +"\"><a title=\"/"+row['title'] +"\" href=\"/"+ section + "/" + row['href']+"\"><span>"+row['title'].title()+"</span></a></li>"