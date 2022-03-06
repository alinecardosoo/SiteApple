# -*- coding: utf-8 -*-
from Globals import package_home
from OFS import SimpleItem
from Products.ZSQLMethods.SQL import SQL
from Globals import DTMLFile
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
import os


global product_path
product_path = os.path.join(package_home(globals())) + '/'


class Avaliacoes (SimpleItem.SimpleItem):


	"""Objeto apple"""

	meta_type = 'Avaliacoes' 


	def __init__(self, id):

		"""Initialize"""
		self.id = id
		

	#detalhes produto
	def detail_product(self, id_produto):

		"""redirecionamento pagina de detalhes"""
		d = self.select_detalhe(id_produto=id_produto)
		return d

	#adicionando avaliacoes dos produtos
	def add_detail(self, nome_complete, id_produto, opinioes):

		"""insere avaliacao"""
		self.insert_avaliacao(nome_complete=nome_complete, id_produto=id_produto, opinioes=opinioes)
		return 

	def view_avaliation(self):

		"""avaliacoes"""
		selc = self.selct_av_produto()
		return

	def update_select(self, id_produto):

		"""update select"""

		edit_select = self.select_detalhe(id_produto=id_produto)

		return edit_select

	def delete_av(self, id_produto):

		"""deletando avaliacao"""
		self.delete_avaliacao(id_produto=id_produto)
		return 

	#select dos detalhes do produto
	select_detalhe = SQL(id='select_detalhe', title='', 
		connection_id="connection", 
		arguments='id_produto', 
		template=open(product_path + 'query/select_detalhe.sql').read())

	#inserindo avaliacoes
	insert_avaliacao = SQL(id='insert_avaliacao', title='', 
		connection_id="connection", 
		arguments='nome_complete\nid_produto\nopinioes', 
		template=open(product_path + 'query/insert_avaliacao.sql').read())

	#select das avaliaoes
	selct_av_produto = SQL(id='selct_av_produto', title='', 
		connection_id="connection", 
		arguments='id_produto', 
		template=open(product_path + 'query/selct_av_produto.sql').read())

	#delete avaliacao
	delete_avaliacao = SQL(id='delete_avaliacao', title='', 
		connection_id="connection", 
		arguments='id_produto', 
		template=open(product_path + 'query/delet_avaliacao.sql').read())