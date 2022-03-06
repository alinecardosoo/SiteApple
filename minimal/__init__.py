import minimal

def initialize(context):

	"""Inicializando o meu minimal para aparecer na lista de produtos do zope"""

	context.registerClass(

		minimal.minimal,
		
		constructors = (

			minimal.manage_addMinimalForm,
			minimal.manage_addminimalAction,

			),
			icon=None

		)
