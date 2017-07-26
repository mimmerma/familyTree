#
#
#
class Person():
	def __init__(self, namePerson, birthDate, nameFirstParent, nameSecondParent):
		self.namePerson = namePerson
		self.birthDate = birthDate
		self.nameFirstParent = nameFirstParent
		# do I want to check for the condition that nameSecondParent != ''
		self.nameSecondParent = nameSecondParent

		self.children = []
#
#
#