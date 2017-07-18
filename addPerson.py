#
#
#
import re

def validateInput(userInput):
	# allow for more than two parents?
	
	# familyTree.py -a addPerson -n <namePerson> -b <birthDate> -f <nameFirstParent> -s <nameSecondParent>
	# Ex: familyTree.py -a addPerson -n Jason Immerman -b 05/22/1988 -f Irene Immerman -s Michael Immerman
	# default of nameSecondParent is '' if not omitted
	
	# unpack userInput
	action, namePerson, birthDate, nameFirstParent, nameSecondParent, nameDeceased, deathDate = userInput

	if nameDeceased != '' or deathDate != '':
		raise Exception('nameDeceased and deathDate are not allowable arguments for the addPerson action')

	# remove leading and trailing whitespace
	namePerson.strip()
	birthDate.strip()
	nameFirstParent.strip()
	if nameSecondParent is not None:
		nameSecondParent.strip()

	# alternative of asking for forgiveness instead of permission
	#try:
	#	nameSecondParent.strip()
	#except AttributeError:
	#	pass

	if namePerson == '' or birthDate == '' or nameFirstParent == '':
		raise Exception('namePerson, birthDate, and nameFirstParent are required for the addPerson action')

	# a character class [...] matches any character in the class
	# \W matches any non-alphanumeric character, equivalent to the class [^a-zA-Z0-9_]
	# \d matches any decimal digit, equivalent to [0-9]
	# compilation flags: re.I sets IGNORECASE and re.X sets VERBOSE (enables RE's to be on multiple lines)
	# search method finds pattern anywhere in string
	namePerson = re.sub(r',', ' ', namePerson)
	namePerson_noSpace = re.sub(r'\s+', '', namePerson)
	# pattern object for invalidChars
	p_invalidChars = re.compile(r'[\W_\d]', re.I | re.X)
	m_namePerson = p_invalidChars.search(namePerson_noSpace)
	if m_namePerson:
		raise Exception('there are either non-alphanumeric characters, underscore, or digits in namePerson')

	# match method finds pattern at the beginning of the string
	birthDate_noSpace = re.sub(r'\s+', '', birthDate)
	# pattern object for birthDate_format
	p_birthDate_format = re.compile(r'\d\d/\d\d/\d\d\d\d')
	m_birthDate_format = p_birthDate_format.match(birthDate_noSpace)
	if not m_birthDate_format:
		raise Exception('birthDate is not in the proper format: mm/dd/yyyy')
	
	nameFirstParent = re.sub(r',', ' ', nameFirstParent)
	nameFirstParent_noSpace = re.sub(r'\s+', '', nameFirstParent)
	# pattern object for invalidChars
	m_nameFirstParent = p_invalidChars.search(nameFirstParent_noSpace)
	if m_nameFirstParent:
		raise Exception('there are either non-alphanumeric characters, underscore, or digits in nameFirstParent')
	
	if nameSecondParent is not None:
		nameSecondParent = re.sub(r',', ' ', nameSecondParent)
		nameSecondParent_noSpace = re.sub(r'\s+', '', nameSecondParent)
		# pattern object for invalidChars
		m_nameSecondParent = p_invalidChars.search(nameSecondParent_noSpace)
		if m_nameSecondParent:
			raise Exception('there are either non-alphanumeric characters, underscore, or digits in nameSecondParent')

	#return args for addPerson action with whitespace stripped, first and last names space delimited
	return namePerson, birthDate, nameFirstParent, nameSecondParent

def getHelp():
	print('familyTree.py -a addPerson -n <namePerson> -b <birthDate> -f <nameFirstParent> -s <nameSecondParent>')

#def execute():

#
#
#