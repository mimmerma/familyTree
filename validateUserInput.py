#
#
#
import re

# should I use assert statements (that raise an AssertionError if they are False) OR case statements with raise Exception('...')
# functionalize this code into smaller codeblocks?
# allow for optional birthDate? Does not currently

def testInputFormat(userInput):
	"""Validates the format of the user input.
		Doesn't validate that the action is legal (this will probably occur within the methods themselves).
		For example, this won't handle if the user calls the deathNotice method on a nonexistent Person."""

	# 'is' operator tests whether two objects are the same thing, not just the same value
	# note that str is an identifier and not itself a string
	if type(userInput) is not str:
		raise Exception('user input is the wrong type, not a string')
	
	if userInput == '':
		raise Exception('no input entered')

	# remove leading and trailing spaces
	# use built-in strip() function?
	userInput = re.sub(r'\A\s*', '', userInput)
	userInput = re.sub(r'\s*\Z', '' , userInput)

	userInputList = userInput.split(',')
	methodCalled = userInputList[0]

	if methodCalled == 'addPerson':
		namePerson, birthDate, nameFirstParent, nameSecondParent = addPersonValidate(userInputList)
		return methodCalled, namePerson, birthDate, nameFirstParent, nameSecondParent
	elif methodCalled == 'deathNotice':
		nameDeceased, deathDate = deathNoticeValidate(userInputList)
		return methodCalled, nameDeceased, deathDate
	elif methodCalled == 'displayTree':
		displayTreeValidate(userInputList)
		return methodCalled
	else:
		raise Exception('invalid method, miscreant')

def addPersonValidate(userInputList):
	# allow for more than two parents?
	# addPerson method: <name-of-person>, <birth-date>, <name-of-first-parent>, [<optional-name-of-second-parent>]
	# Ex: addPerson, Jason Immerman, 05/22/1988, Irene Immerman, Michael Immerman
	if len(userInputList) == 4:
		_, namePerson, birthDate, nameFirstParent = userInputList
		# default of nameSecondParent is None if not omitted
		nameSecondParent = None
	elif len(userInputList) == 5:
		_, namePerson, birthDate, nameFirstParent, nameSecondParent = userInputList
	
	# remove leading and trailing whitespace
	namePerson.strip()
	birthDate.strip()
	nameFirstParent.strip()
	try:
		nameSecondParent.strip()
	except AttributeError:
		pass
	
	# pattern object for invalidChars
	# a character class [...] matches any character in the class
	# \W matches any non-alphanumeric character, equivalent to the class [^a-zA-Z0-9_]
	# \d matches any decimal digit, equivalent to [0-9]
	# compilation flags: re.I sets IGNORECASE and re.X sets VERBOSE (enables RE's to be on multiple lines)
	# search method finds pattern anywhere in string
	namePerson_noSpace = re.sub(r'\s+', '', namePerson)
	p_invalidChars = re.compile(r'[\W_\d]', re.I | re.X)
	m_namePerson = p_invalidChars.search(namePerson_noSpace)
	if m_namePerson:
		raise Exception('there are either non-alphanumeric characters, underscore, or digits in namePerson')

	# pattern object for birthDate_format
	# match method finds pattern at the beginning of the string
	# allow for extra whitspace within birthDate? Currently does allow
	birthDate_noSpace = re.sub(r'\s+', '', birthDate)
	p_birthDate_format = re.compile(r'\d\d/\d\d/\d\d\d\d')
	m_birthDate_format = p_birthDate_format.match(birthDate_noSpace)
	if not m_birthDate_format:
		raise Exception('birthDate is not in the proper format: mm/dd/yyyy')
	
	# pattern object for invalidChars
	nameFirstParent_noSpace = re.sub(r'\s+', '', nameFirstParent)
	m_nameFirstParent = p_invalidChars.search(nameFirstParent_noSpace)
	if m_nameFirstParent:
		raise Exception('there are either non-alphanumeric characters, underscore, or digits in nameFirstParent')
	
	if nameSecondParent is not None:
		# pattern object for invalidChars
		nameSecondParent_noSpace = re.sub(r'\s+', '', nameSecondParent)
		m_nameSecondParent = p_invalidChars.search(nameSecondParent_noSpace)
		if m_nameSecondParent:
			raise Exception('there are either non-alphanumeric characters, underscore, or digits in nameSecondParent')

	return namePerson, birthDate, nameFirstParent, nameSecondParent

def deathNoticeValidate(userInputList):
	# deathNotice method: <name-of-deceased>, [<optional-date-of-death>]
	# Ex: deathNotice, David Bowie, 01/10/2016
	# Note about deathNotice: must be called with name of existing Person object
	# Note about deathNotice: date-of-death is optional because might be unknown
	if len(userInputList) == 2:
		_, nameDeceased = userInputList
		# default of deathDate is None if not omitted
		deathDate = None
	elif len(userInputList) == 3:
		_, nameDeceased, deathDate = userInputList
	
	# remove leading and trailing whitespace
	nameDeceased.strip()
	try:
		deathDate.strip()
	except AttributeError:
		pass

	# pattern object for invalidChars
	nameDeceased_noSpace = re.sub(r'\s+', '', nameDeceased)
	p_invalidChars = re.compile(r'[\W_\d]', re.I | re.X)
	m_nameDeceased = p_invalidChars.search(nameDeceased_noSpace)
	if m_nameDeceased:
		raise Exception('there are either non-alphanumeric characters, underscore, or digits in nameDeceased')

	if deathDate is not None:
		# pattern object for deathDate_format
		deathDate_noSpace = re.sub(r'\s+', '', deathDate)
		p_deathDate_format = re.compile(r'\d\d/\d\d/\d\d\d\d')
		m_deathDate_format = p_deathDate_format.match(deathDate_noSpace)
		if not m_deathDate_format:
			raise Exception('deathDate is not in the proper format: mm/dd/yyyy')

	return nameDeceased, deathDate

def displayTreeValidate(userInputList):
	# displayTree method takes no arguments')
	# Ex: displayTree
	if len(userInputList) > 1:
		raise Exception('displayTree method takes no arguments')
#
#
#