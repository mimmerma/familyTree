#
#
#
import re

def validateInput(userInput):
	# familyTree.py -a deathNotice -d <nameDeceased> -e <deathDate>
	# Ex: familyTree.py -a deathNotice -d David Bowie -e 01/10/2016
	# Note about deathNotice: date-of-death is optional because might be unknown
	
	# need to implement the following validation once execute() methods are implemented
	# Note about deathNotice: must be called with name of existing Person object

	# unpack userInput
	action, namePerson, birthDate, nameFirstParent, nameSecondParent, nameDeceased, deathDate = userInput
	
	if namePerson != '' or birthDate != '' or nameFirstParent != '' or nameSecondParent != '':
		raise Exception('namePerson, birthDate, nameFirstParent, nameSecondParent are not allowable arguments for the deathNotice action')

	# remove leading and trailing whitespace
	nameDeceased.strip()
	if deathDate is not None:
		deathDate.strip()

	if nameDeceased == '' or deathDate == '':
		raise Exception('nameDeceased and deathDate are required for the deathNotice action')

	#try:
	#	deathDate.strip()
	#except AttributeError:
	#	pass

	nameDeceased = re.sub(r',', ' ', nameDeceased)
	nameDeceased_noSpace = re.sub(r'\s+', '', nameDeceased)
	# pattern object for invalidChars
	p_invalidChars = re.compile(r'[\W_\d]', re.I | re.X)
	m_nameDeceased = p_invalidChars.search(nameDeceased_noSpace)
	if m_nameDeceased:
		raise Exception('there are either non-alphanumeric characters, underscore, or digits in nameDeceased')

	if deathDate is not None:
		deathDate_noSpace = re.sub(r'\s+', '', deathDate)
		# pattern object for deathDate_format
		p_deathDate_format = re.compile(r'\d\d/\d\d/\d\d\d\d')
		m_deathDate_format = p_deathDate_format.match(deathDate_noSpace)
		if not m_deathDate_format:
			raise Exception('deathDate is not in the proper format: mm/dd/yyyy')

	#return args for addPerson action with whitespace stripped, first and last names space delimited
	return nameDeceased, deathDate

def getHelp():
	print('familyTree.py -a deathNotice -d <nameDeceased> -e <deathDate>')

#def execute():

#
#
#