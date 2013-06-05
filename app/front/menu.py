# -*- coding: utf-8 -*-

from django.utils.encoding import smart_str
from app.programas.models import Program
from app.youtube.models import Categoria


class Menu(object):

	items = [			
			{				
				'href': 'inicio',
				'title': 'inicio',				
			},
			{				
				'href': 'nosotros',
				'title': 'nosotros',				
			},
			{				
				'href': 'programas',
				'title': 'programas',
				'child':[
					{
						'href': 'reciclases',
						'title': 'Reciclases',
					},	
					{
						'href': 'reciclases',
						'title': 'Reciclases en tu jardín',
					},
					{
						'href': 'reciclases',
						'title': 'Proyecto Semilla',
					},
					{
						'href': 'reciclases',
						'title': 'Jóvenes transformando',
					},
					{
						'href': 'reciclases',
						'title': 'Ecoagentes',
					},
					{
						'href': 'reciclases',
						'title': 'Laboratorio Vivo',
					},
				],
			},
			{				
				'href': 'ecotips',
				'title': 'ecotips',
			},
			{				
				'href': 'transparencia',
				'title': 'transparencia',				
			},
			{				
				'href': 'talleristas',
				'title': 'talleristas',				
			},
			{				
				'href': 'campanas_donantes',
				'title': 'Campañas y donantes',
			},			
			{				
				'href': 'contacto',
				'title': 'contacto',
			},
		]


	def get_main(self, section):
		response = ''		
		for row in self.items:
			if row['href'] == section:
				response += "<li class=\"current \"><a title=\"/"+row['title'] +"\" href=\"/"+row['href']+"\"><span>"+row['title'].title()+"</span></a></li>"
			#	if "child" in name 
			#		get_child(self, row['href'], self.items)
			else:
				response += "<li><a title=\"/"+row['title'] +"\" href=\"/"+row['href']+"\"><span>"+row['title'].title()+"</span></a></li>"

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