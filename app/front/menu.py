# -*- coding: utf-8 -*-

from django.utils.encoding import smart_str


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
				'href': 'inversiones_sociales',
				'title': 'inversiones sociales',
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
			else:
				response += "<li><a title=\"/"+row['title'] +"\" href=\"/"+row['href']+"\"><span>"+row['title'].title()+"</span></a></li>"

		if len(response):
			response = "<ul class=\"menu\">" + response + "</ul>"
		return response
'''
	def get_footer(self, section):
		response = ''		
		for row in self.items:
			if row['href'] not in 'testimoniales,contacto':
				child = self.get_child(row['href'], row['child']) if row.has_key('child') else ''
				if row['href'] == section:
					response += "<li class=\"active \"><a title=\"/"+row['title'] +"\" href=\"/"+row['href']+"\">"+row['title'].title()+"</a> "+ child +"</li>"
				else:
					response += "<li><a title=\"/"+row['title'] +"\" href=\"/"+row['href']+"\">"+row['title'].title()+"</a>"+ child +"</li>"					
		if len(response):
			response = "<ul>" + response + "</ul>"
		return response

	def get_child(self, section, data):
		response = ''		
		if section != 'galeria':		
			for row in data:
				li_id = row['li_id'] if row.has_key('li_id') else ''						
				response += "<li id=\""+ li_id +"\"><a title=\"/"+row['title'] +"\" href=\"/"+ section + "/" + row['href']+"\"><span>"+row['title'].title()+"</span></a></li>"		
		else:			
			category = Category.objects.filter(active=True)			
			for row in category:
				response += "<li><a title=\""+ smart_str(row.name) + "\" href=\"/galeria/"+ str(row.url) + "\"><span>" + smart_str(row.name) +"</span></a></li>"
		if len(response):
			response = "<ul>" + response + "</ul>"
		return response

	def get_galeria(self):
		response = ''		
		category = Category.objects.filter(active=True)			
		first = ''
		second = ''
		third = ''
		i = 0
		for row in category:
			if i % 3 == 0:
				if len(first):
					first += "<li><a href=\"/galeria/"+ str(row.url) + "\" title=\"" + smart_str(row.name)  + "\"><span>"+ smart_str(row.name) +"</span></a></li>"
				else:
					first += "<li class=\"first\"><a href=\"/galeria/"+ str(row.url) + "\" title=\"" + smart_str(row.name)  + "\"><span>"+ smart_str(row.name) +"</span></a></li>"			
			elif i % 3 == 1:
				if len(second):
					second += "<li><a href=\"/galeria/"+ str(row.url) + "\" title=\"" + smart_str(row.name)  + "\"><span>"+ smart_str(row.name) +"</span></a></li>"
				else:
					second += "<li class=\"first\"><a href=\"/galeria/"+ str(row.url) + "\" title=\"" + smart_str(row.name)  + "\"><span>"+ smart_str(row.name) +"</span></a></li>"
			elif i % 3 == 2:
				if len(third):
					third += "<li><a href=\"/galeria/"+ str(row.url) + "\" title=\"" + smart_str(row.name)  + "\"><span>"+ smart_str(row.name) +"</span></a></li>"
				else:
					third += "<li class=\"first\"><a href=\"/galeria/"+ str(row.url) + "\" title=\"" + smart_str(row.name)  + "\"><span>"+ smart_str(row.name) +"</span></a></li>"
			i += 1
		response = "<div class=\"column one_third first\"><ul><ul>" + first + "</ul></div><div class=\"column one_third first\"><ul><ul>" + second + "</ul></div><div class=\"column one_third first\"><ul><ul>" + third + "</ul></div>"	
		return response
'''