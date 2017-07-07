#
#
#
import rlcompleter

displayHelp():
	'''displays help message explaining user input format
		\nprint message when 1. user requests OR 2. user enters invalid information'''
	helpMessage = '''\nWelcome to Family Tree!
						\nPlease enter info to begin or continue building your tree, or to display it
						\nEntries should be in the form [method], [<optional-arguments comma delimited>]
						\nPossible methods are: "addPerson", "deathNotice", "displayTree"

						\naddPerson method: <name-of-person>, <birth-date>, <name-of-first-parent>, [<optional-name-of-second-parent>]
						\nEx: addPerson, Jason Immerman, 05/22/1988, Irene Immerman, Michael Immerman

						\ndeathNotice method: <name-of-deceased>, [<optional-date-of-death>]
						\nEx: deathNotice, David Bowie, 01/10/2016
						\nNote about deathNotice: must be called with name of existing Person object
						\nNote about deathNotice: date-of-death is optional because might be unknown

						\ndisplayTree method takes no arguments
						\nEx: displayTree
						\n'''

	print(helpMessage)

promptUser():
	'''prompt for user input in form described in intro'''
	rawInputPrompt = '[method], [<optional-arguments-comma-delimited>] --> '
	userInput = raw_input(rawInputPrompt)

	print('you entered: ', userInput)

displayHelp()
promptUser()
#
#
#