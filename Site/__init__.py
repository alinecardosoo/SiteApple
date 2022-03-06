import apple


def initialize(context):

	"""Inicializando"""

	context.registerClass(

	apple.apple,

	constructors=(

		apple.manage_addAppleForm,
		apple.manage_add_apple

		)
	)