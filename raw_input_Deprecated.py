#
#
#
import rlcompleter
import validateUserInput as validateUserInput

def printIntro():
	# intro
	# put in 'help' section?
	print
	print('Welcome to Family Tree!')
	print('Please enter info to begin or continue building your tree, or to display it')
	print('Entries should be in the form [method], [<optional-arguments comma delimited>]')
	print('Possible methods are: "addPerson", "deathNotice", "displayTree"')
	print
	print('addPerson method: <name-of-person>, <birth-date>, <name-of-first-parent>, [<optional-name-of-second-parent>]')
	print('Ex: addPerson, Jason Immerman, 05/22/1988, Irene Immerman, Michael Immerman')
	print
	print('deathNotice method: <name-of-deceased>, [<optional-date-of-death>]')
	print('Ex: deathNotice, David Bowie, 01/10/2016')
	print('Note about deathNotice: must be called with name of existing Person object')
	print('Note about deathNotice: date-of-death is optional because might be unknown')

	print
	print('displayTree method takes no arguments')
	print('Ex: displayTree')
	print('\n')

def userInputPrompt():
	# will have to loop the prompt or place inside function to be called in a loop
	# prompt for user input in form described in intro
	userInput = raw_input('[method], [<optional-arguments-comma-delimited>] --> ')

	print('you entered: ', userInput)

	return userInput

printIntro()

userInput = userInputPrompt()

# validate the types and formats of userInput
userInputList = validateUserInput.testInputFormat(userInput)
if len(userInputList) == 5:
	methodCalled, namePerson, birthDate, nameFirstParent, nameSecondParent = userInputList
if len(userInputList) == 3:
	methodCalled, nameDeceased, deathDate = userInputList
if len(userInputList) == 1:
	methodCalled = userInputList[0]
#
#
#