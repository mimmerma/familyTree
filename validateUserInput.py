#
#
#
import re
import addPerson as addPerson
import deathNotice as deathNotice
import displayTree as displayTree

# allow for optional birthDate? Does not currently - add issue ticket to backlog

def testInputFormat(userInput):
	"""Validates the format of the user input.
		Doesn't validate that the action is legal (this will probably occur within the methods themselves).
		For example, this won't handle if the user calls the deathNotice method on a nonexistent Person."""

	# 'is' operator tests whether two objects are the same thing, not just the same value
	# note that str is an identifier and not itself a string
	if userInput == None:
		raise Exception('user input is None')
	
	#if type(userInput) is not str:
	#	raise Exception('user input is the wrong type, not a string')
	
	#if userInput == '':
	#	raise Exception('user input is empty string')

	if userInput == ():
		raise Exception('user input is empty tuple')

	# remove leading and trailing spaces
	# regex alternative
	#userInput = re.sub(r'\A\s*', '', userInput)
	#userInput = re.sub(r'\s*\Z', '' , userInput)
	# use built in strip() method instead of regex for automatic optimizations
	#userInput.strip()

	# unpack action from userInput
	action, _, _, _, _, _, _ = userInput

	# remove leading and trailing whitespace from action
	action.strip()

	# store action name strings in variables (make sure doesn't conflict with module names)
	addPerson_action = 'addPerson'
	deathNotice_action = 'deathNotice'
	displayTree_action = 'displayTree'

	# should I put the validateInput code within the constructor for the AddPerson class or call as an explicit method as below
	# is there some way to call the validateInput method of the AddPerson class without instantiating it as addPersonCall?
	if action == addPerson_action:
		namePerson, birthDate, nameFirstParent, nameSecondParent = addPerson.validateInput(userInput)
		# test output
		print('processed input: ')
		print('action is:', action, 'namePerson is:', namePerson, 'birthDate is:', birthDate, 'nameFirstParent is:', nameFirstParent,
			'nameSecondParent is:', nameSecondParent)
	elif action == deathNotice_action:
		nameDeceased, deathDate = deathNotice.validateInput(userInput)
		# test output
		print('processed input: ')
		print('action is:', action, 'nameDeceased is:', nameDeceased, 'deathDate is:', deathDate)
	elif action == displayTree_action:
		displayTree.validateInput(userInput)
	else:
		raise Exception('invalid action')
#
#
#