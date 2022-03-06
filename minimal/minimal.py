# -*- coding: utf-8 -*-

from OFS import SimpleItem
from Globals import DTMLFile

class minimal(SimpleItem.SimpleItem):

	"""minimal object"""


	meta_type = 'minimal' 

	manage_options = (

		{'label': 'Properties', 'action': 'manage_editForm',},
		{'label': 'View', 'action': 'index_html',},
	)
		

	def __init__(self, id, title, content):

		self.id = id # obrigatorio o id
		self.title = title
		self.content = content

	
	def manage_editAction(self, title, content, RESPONSE=None):

		self.title = title
		self.content = content
		self._p_changed = 1
		RESPONSE.redirect('manage_editForm')

	def teste(self):

		"""teste."""

		return "ABC"


	#usado para visualizar o conteudo do objeto

	index_html = DTMLFile('www/index_html', globals())

	manage_editForm = DTMLFile('www/manage_editForm', globals())


def manage_addminimalAction(self, id='minimal', title='Title here', content='content here', REQUEST=None):

		"""Adiciandndo o minimal a uma pasta"""

		self._setObject(id, minimal(id, title, content))

		if REQUEST is not None:
			return self.manage_main(self,REQUEST)

manage_addMinimalForm = DTMLFile('www/manage_addMinimalForm', globals())
	

	