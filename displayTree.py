#
#
#
def validateInput(userInput):
	# displayTree action takes no arguments
	# Ex: displayTree

	# unpack userInput
	action, namePerson, birthDate, nameFirstParent, nameSecondParent, nameDeceased, deathDate = userInput

	for param in userInput[1:]:
		if param != '':
			raise Exception('no arguments allowable for the displayTree action')

	# displayTree action not implemented yet
	raise Exception('NotImplementedError')

def getHelp():
	print('familyTree.py -a displayTree')

#def execute():

#
#
#