# -*- coding: utf-8 -*-
from Globals import package_home
from OFS import SimpleItem
from Products.ZSQLMethods.SQL import SQL
from Globals import DTMLFile
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
import os


global product_path
product_path = os.path.join(package_home(globals())) + '/'


class Produtos (SimpleItem.SimpleItem):

	"""Objeto apple"""

	meta_type = 'Produtos' 



	def __init__(self, id):

		"""Initialize"""
		self.id = id


	def select_produtos(self):

		"""fazendo select dos produtos"""
		dados = self.select_produto()
		return dados


	def process_register(self, nome, detalhes, preco):

		"""inserindo produto na tabela e reotnando para pagina de produtos"""
		process = self.insert_produto(nome=nome, detalhes=detalhes, preco=preco)
		
		return

	def update_insert(self, nome, detalhes, preco, id_produto):

		"""editando produto"""
		self.update(nome=nome, detalhes=detalhes, preco=preco, id_produto=id_produto)

		return 

	def delete_prod(self, id_produto):

		"""deletando avaliacao"""
		self.delete_produtos(id_produto=id_produto)
		return

	#querys

	#select da lista de produto
	select_produto = SQL(id='select_produto', title='', 
		connection_id="connection", 
		arguments='', 
		template=open(product_path + 'query/select_produto.sql').read())

	#inserindo produtos a lista
	insert_produto = SQL(id='insert_produto', title='', 
		connection_id="connection", 
		arguments='nome\ndetalhes\npreco', 
		template=open(product_path + 'query/insert_produto.sql').read())


	#update products
	update = SQL(id='update', title='', 
		connection_id="connection", 
		arguments='nome\ndetalhes\nopinioes\npreco\nid_produto', 
		template=open(product_path + 'query/update.sql').read())


	#deletando produtos
	delete_produtos = SQL(id='delete_produtos', title='', 
		connection_id="connection", 
		arguments='id_produto', 
		template=open(product_path + 'query/delet_produtos.sql').read())
