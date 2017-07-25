#
#
#
# in order for this getopt approach to work I have to make sure the data for familyTree.py is stored in memory after the program ends

# test if rlcompleter works with getopt to enable bash like command line capabilities
#import rlcompleter
import sys, getopt
import validateUserInput as validateUserInput
import getHelp as getHelp

# first and last names should be comma delimited, e.g. 'Jason,Immerman'
# empty spaces will be interpreted by the command line as the end of a parameter, unless the parameter is wrapped in double quotes
# e.g. 'David Bowie' will be interpreted as ('David', 'Bowie) and
# '"David Bowie"' will be interpreted as ('David Bowie')

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
		opts, args = getopt.getopt(argv, 'ha:n:b:f:s:d:e:', ['action=','namePerson=', 'birthDate=', 'nameFirstParent=', 'nameSecondParent=', 'nameDeceased=', 'deathDate='])
	except getopt.GetoptError:
		getHelp.getHelp_allActions()
		# Unix programs generally use 2 for command line syntax errors and 1 for all other kind of errors
		sys.exit(2)
	for opt, arg in opts:
		# strip whitespace from option
		opt = opt.strip()
		# optional help option
		if opt == '-h':
			getHelp.getHelp_allActions()
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
	#print('unprocessed input: ')
	#print('action is:', action, 'namePerson is:', namePerson, 'birthDate is:', birthDate, 'nameFirstParent is:', nameFirstParent,
	#		'nameSecondParent is:', nameSecondParent, 'nameDeceased is:', nameDeceased, 'deathDate is:', deathDate)

	userInput = (action, namePerson, birthDate, nameFirstParent, nameSecondParent, nameDeceased, deathDate)
	return userInput

# need clarification
if __name__ == '__main__':
	# sys.argv[1:] captures all the userInputs excluding the script name
	userInput = main(sys.argv[1:])

# validate user input for any of the actions
validateUserInput.testInputFormat(userInput)
#
#
#