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
						'href': 'aliados-estrategicos',
						'title': 'Aliados estrat&eacute;gicos',
					},	
					{
						'href': 'universidades',
						'title': 'Universidades',
					},
					{
						'href': 'inversionistas-sociales',
						'title': 'Inversionistas Sociales',
					},
					{
						'href': 'especie',
						'title': 'Especie',
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
				programas = Program.objects.all()
				for row2 in programas:
					child +=  "<li><a title=\""+row2.title +"\" href=\"/"+row['href']+"/"+slugify(row2.title)+"\"><span>"+row2.title+"</span></a></li>"
			
			elif row['href'] == 'campanas_donantes' and 'child' in row:
				for row2 in row['child']:
					child +=  "<li><a title=\""+row2['title']+"\" href=\"/"+row['href']+"/"+row2['href']+"\"><span>"+row2['title']+"</span></a></li>"

			if len(child):
				child = "<ul class=\"child\">" + child + "</ul>"

			if row['href'] == section:
				response += "<li class=\"current \"><a title=\"/"+row['title'] +"\" href=\"/"+row['href']+"\"><span>"+row['title']+"</span></a> " + child + "</li>"
			else:
				response += "<li><a title=\"/"+row['title'] +"\" href=\"/"+row['href']+"\"><span>"+row['title']+"</span></a> " + child + "</li>"

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