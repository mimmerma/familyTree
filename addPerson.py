#
#
#
import re
import getHelp as getHelp
import personClass as personClass

def validateInput(userInput):
	# familyTree.py -a addPerson -n <namePerson> -b <birthDate> -f <nameFirstParent> -s <nameSecondParent>
	# Ex: familyTree.py -a addPerson -n Jason Immerman -b 05/22/1988 -f Irene Immerman -s Michael Immerman
	# default of nameSecondParent is '' if not omitted
	
	# unpack userInput
	action, namePerson, birthDate, nameFirstParent, nameSecondParent, nameDeceased, deathDate = userInput

	if nameDeceased != '' or deathDate != '':
		raise Exception('nameDeceased and deathDate are not allowable arguments for the addPerson action')

	# remove leading and trailing whitespace
	namePerson = namePerson.strip()
	birthDate = birthDate.strip()
	nameFirstParent = nameFirstParent.strip()
	if nameSecondParent is not None:
		nameSecondParent = nameSecondParent.strip()

	if namePerson == '' or birthDate == '' or nameFirstParent == '':
		raise Exception('namePerson, birthDate, and nameFirstParent are required for the addPerson action')

	validateNamePerson(namePerson)

	validateBirthDate(birthDate)

	validateNameFirstParent(nameFirstParent)

	if nameSecondParent is not None:
		validateNameSecondParent(nameSecondParent)

	#return args for addPerson action with whitespace stripped, first and last names space delimited
	return namePerson, birthDate, nameFirstParent, nameSecondParent

def validateNamePerson(namePerson):
	# replace comma with space in name if comma delimited, otherwise do nothing
	namePerson = re.sub(r',', ' ', namePerson)
	namePerson_noSpace = re.sub(r'\s+', '', namePerson)
	# pattern object for invalidChars
	p_invalidChars = re.compile(r'[\W_\d]', re.I | re.X)
	m_namePerson = p_invalidChars.search(namePerson_noSpace)
	if m_namePerson:
		raise Exception('there are either non-alphanumeric characters, underscore, or digits in namePerson')

def validateBirthDate(birthDate):
	birthDate_noSpace = re.sub(r'\s+', '', birthDate)
	# pattern object for birthDate_format
	p_birthDate_format = re.compile(r'\d\d/\d\d/\d\d\d\d')
	m_birthDate_format = p_birthDate_format.match(birthDate_noSpace)
	if not m_birthDate_format:
		raise Exception('birthDate is not in the proper format: mm/dd/yyyy')
	
def validateNameFirstParent(nameFirstParent):
	# replace comma with space in name if comma delimited, otherwise do nothing
	nameFirstParent = re.sub(r',', ' ', nameFirstParent)
	nameFirstParent_noSpace = re.sub(r'\s+', '', nameFirstParent)
	# pattern object for invalidChars
	m_nameFirstParent = p_invalidChars.search(nameFirstParent_noSpace)
	if m_nameFirstParent:
		raise Exception('there are either non-alphanumeric characters, underscore, or digits in nameFirstParent')

def validateNameSecondParent(nameSecondParent):
	# replace comma with space in name if comma delimited, otherwise do nothing
	nameSecondParent = re.sub(r',', ' ', nameSecondParent)
	nameSecondParent_noSpace = re.sub(r'\s+', '', nameSecondParent)
	# pattern object for invalidChars
	m_nameSecondParent = p_invalidChars.search(nameSecondParent_noSpace)
	if m_nameSecondParent:
		raise Exception('there are either non-alphanumeric characters, underscore, or digits in nameSecondParent')

def getHelp():
	getHelp.getHelp_addPerson()

def execute(namePerson, birthDate, nameFirstParent, nameSecondParent, personHash):
	newPerson = personClass.Person(namePerson, birthDate, nameFirstParent, nameSecondParent)
	personHash[newPerson.namePerson] = newPerson
	return personHash
#
#
#