#
#
#
def getHelp_allActions():
	allActions = '''
				familyTree.py -a <action> -n <namePerson> -b <birthDate> -f <nameFirstParent> -s <nameSecondParent> -d <nameDeceased> -e <deathDate>
				\nfamilyTree.py -a addPerson -n <namePerson> -b <birthDate> -f <nameFirstParent> -s <nameSecondParent>
				\nfamilyTree.py -a deathNotice -d <nameDeceased> -e <deathDate>
				\nfamilyTree.py -a displayTree
	'''
	print(allActions)

def getHelp_addPerson():
	addPersonHelp = '''
					familyTree.py -a addPerson -n <namePerson> -b <birthDate> -f <nameFirstParent> -s <nameSecondParent>
					\nEx: familyTree.py -a addPerson -n Jason Immerman -b 05/22/1988 -f Irene Immerman -s Michael Immerman
					\ndefault of nameSecondParent is '' if not omitted
	'''
	print(addPersonHelp)
def getHelp_deathNotice():
	deathNoticeHelp = '''
						familyTree.py -a deathNotice -d <nameDeceased> -e <deathDate>
						\nEx: familyTree.py -a deathNotice -d David Bowie -e 01/10/2016
						\ndate-of-death is optional because might be unknown
						\nmust be called with name of existing Person object
	'''
	print(deathNoticeHelp)
def getHelp_displayTree():
	displayTreeHelp = '''
						displayTree action takes no arguments
						\nEx: familyTree.py -a displayTree
	'''
	print(displayTreeHelp)
#
#
#