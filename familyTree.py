#
#
#
# in order for this getopt approach to work I have to make sure the data for familyTree.py is stored in memory after the program ends

# test if rlcompleter works with getopt to enable bash like command line capabilities
#import rlcompleter
import sys, getopt
import validateUserInput as validateUserInput

def main(argv):
	'''main familyTree.py script'''
	# assign possible argument identifiers to empty string
	action = ''
	namePerson = ''
	birthDate = ''
	nameFirstParent = ''
	nameSecondParent = ''
	nameDeceased = ''
	deathDate = ''
	try:
		# argv is argument list (argv[0] is script name)
		# short options are in a string followed by ':' if they require an argument (stored in '-<shortOption>')
		# long options are in a list of strings followed by equal (stored in '--<longOption>')
		# first and last names should be comma delimited, e.g. 'Jason,Immerman'
		# empty spaces will be interpreted by the command line as the end of a parameter
		# should delete remove spaces from validations
		opts, args = getopt.getopt(argv, 'ha:n:b:f:s:d:e:', ['action=','namePerson=', 'birthDate=', 'nameFirstParent=', 'nameSecondParent=', 'nameDeceased=', 'deathDate='])
	except getopt.GetoptError:
		print('familyTree.py -a <action> -n <namePerson> -b <birthDate> -f <nameFirstParent> -s <nameSecondParent> -d <nameDeceased> -e <deathDate>')
		# Unix programs generally use 2 for command line syntax errors and 1 for all other kind of errors
		sys.exit(2)
	for opt, arg in opts:
		# optional help option
		if opt == '-h':
			print('familyTree.py -a <action> -n <namePerson> -b <birthDate> -f <nameFirstParent> -s <nameSecondParent> -d <nameDeceased> -e <deathDate>')
		# action option required for all program calls
		# possible actions: addPerson, deathNotice, displayTree
		elif opt in ('-a', '--action'):
			action = arg
		# options for addPerson action
		elif opt in ('-n', '--namePerson'):
			namePerson = arg
		elif opt in ('-b', '--birthDate'):
			birthDate = arg
		elif opt in ('-f', '--nameFirstParent'):
			nameFirstParent = arg
		elif opt in ('-s', '--nameSecondParent'):
			nameSecondParent = arg
		# options for deathNotice action
		elif opt in ('-d', '--nameDeceased'):
			nameDeceased = arg
		elif opt in ('-e', '--deathDate'):
			deathDate = arg
	
	# test output
	print('unprocessed input: ')
	print('action is:', action, 'namePerson is:', namePerson, 'birthDate is:', birthDate, 'nameFirstParent is:', nameFirstParent,
			'nameSecondParent is:', nameSecondParent, 'nameDeceased is:', nameDeceased, 'deathDate is:', deathDate)

	userInput = (action, namePerson, birthDate, nameFirstParent, nameSecondParent, nameDeceased, deathDate)
	return userInput

# need clarification
if __name__ == '__main__':
	# sys.argv[1:] captures all the userInputs excluding the script name
	userInput = main(sys.argv[1:])

# validate user input for any of the actions
validateUserInput.testInputFormat(userInput)



#def printIntro():
	# put in 'help' section?
#	print
#	print('Welcome to Family Tree!')
#	print('Please enter info to begin or continue building your tree, or to display it')
#	print('Entries should be in the form [method], [<optional-arguments comma delimited>]')
#	print('Possible methods are: "addPerson", "deathNotice", "displayTree"')
#	print
#	print('addPerson method: <name-of-person>, <birth-date>, <name-of-first-parent>, [<optional-name-of-second-parent>]')
#	print('Ex: addPerson, Jason Immerman, 05/22/1988, Irene Immerman, Michael Immerman')
#	print
#	print('deathNotice method: <name-of-deceased>, [<optional-date-of-death>]')
#	print('Ex: deathNotice, David Bowie, 01/10/2016')
#	print('Note about deathNotice: must be called with name of existing Person object')
#	print('Note about deathNotice: date-of-death is optional because might be unknown')
#
#	print
#	print('displayTree method takes no arguments')
#	print('Ex: displayTree')
#	print('\n')

#printIntro()
#
#
#