# -*- coding: utf-8 -*-

from Globals import package_home
from OFS import SimpleItem
from Globals import DTMLFile
from Products.ZPsycopgDA.DA import Connection
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.ZSQLMethods.SQL import SQL
from controller.main import Main
import os 

global product_path
product_path = os.path.join(package_home(globals())) + '/'


class apple (SimpleItem.SimpleItem):

	"""Objeto apple"""

	main = Main(id='main')
	home = PageTemplateFile('controller/html/home.zpt', globals())

	meta_type = 'Site' 

	manage_options = (

		{'label': 'Properties', 'action': 'index_html'},
		{'label': 'View', 'action': 'index_html',},
	)

	def __init__(self, id, connection):

		"""Initialize"""
		self.id = id
		self.connection = connection

	def get_database_connection(self):

		"""Conexao do banco de dados"""
		return self.connection

	#pagina home
	def index_html(self):

		"""direcionar para minha pagina Home"""
		return self.home()


def manage_add_apple(self, id, connection, RESPONSE):

	"""Adicionando apple em uma pasta"""

	conn = getattr(self,connection)
	self._setObject(id, apple(id,conn))
	RESPONSE.redirect(id+ 'index_html')


manage_addAppleForm = DTMLFile('controller/html/manage_addAppleForm', globals())

