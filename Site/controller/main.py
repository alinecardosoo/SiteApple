from Globals import package_home
from OFS import SimpleItem
from Products.ZSQLMethods.SQL import SQL
from Globals import DTMLFile
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.Site.model.model_produtos.produtos import Produtos
from Products.Site.model.model_avaliacoes.avaliacoes import Avaliacoes
import os


global product_path
product_path = os.path.join(package_home(globals())) + '/'

class Main (SimpleItem.SimpleItem):

	"""Objeto apple"""

	produto = Produtos(id='produto')
	avaliacao = Avaliacoes(id='avaliacao')

	#macros
	head = PageTemplateFile('html/head.zpt', globals())
	ins_avaliacao = PageTemplateFile('html/detalhes/ins_avaliacao', globals())
	selc_avaliacao = PageTemplateFile('html/detalhes/selc_avaliacao', globals())
	footer = PageTemplateFile('html/footer.zpt', globals())
	Template = PageTemplateFile('html/Template.zpt', globals())

	#minhas paginas
	home = PageTemplateFile('html/home.zpt', globals())
	produtos = PageTemplateFile('html/produtos.zpt', globals())
	cadastro = PageTemplateFile('html/cadastro.zpt', globals())
	detalhes = PageTemplateFile('html/detalhes/detalhes.zpt', globals())
	update_page = PageTemplateFile('html/update.zpt', globals())
	siteapple = PageTemplateFile('html/siteapple.js', globals())

	meta_type = 'Main' 


	def __init__(self, id):

		"""Initialize"""
		self.id = id

	
	#todos os produtos
	def product(self):

		"""redirecionar para pagina de Produtos"""
		dados = self.produto.select_produtos()
		return self.produtos(dados=dados)
		
	#cadastro do produto 
	def register(self):
		
		"""redirecionando para cadastro"""
		return self.cadastro()

	#processando cadastro
	def add_cadastro(self, nome, detalhes, preco):

		"""processando dados"""
		process = self.produto.insert_produto(nome=nome, detalhes=detalhes, preco=preco)
		dados = self.produto.select_produtos()
		return self.produtos(dados=dados)

	def details(self, id_produto):

		"""detalhes"""
		d = self.avaliacao.select_detalhe(id_produto=id_produto)
		return self.detalhes(d=d, id_produto=id_produto)

	def add_avaliation(self, nome_complete, id_produto, opinioes):

		"""insere avaliacao"""
		self.avaliacao.insert_avaliacao(nome_complete=nome_complete, id_produto=id_produto, opinioes=opinioes)
		return self.details(id_produto=id_produto)

	def avaliations(self):

		"""avaliacoes"""
		selc = self.avaliacao.selct_av_produto()
		return selc


	def update_product(self, id_produto):

		"""editar"""
		edit_select = self.avaliacao.select_detalhe(id_produto=id_produto)
		return self.update_page(edit_select=edit_select, id_produto=id_produto)

	def edit(self, nome, detalhes, preco, id_produto):

		"""editando produto"""
		self.produto.update(nome=nome, detalhes=detalhes, preco=preco, id_produto=id_produto)

		edit_select = self.avaliacao.select_detalhe(id_produto=id_produto)

		return self.details(id_produto=id_produto)

	
	def delete(self, id_produto):

		"""delete"""
		self.avaliacao.delete_avaliacao(id_produto=id_produto)
		self.produto.delete_produtos(id_produto=id_produto)
		return self.product()
			