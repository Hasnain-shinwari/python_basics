#this code is about positional arguments
#which will pass to the function


def id(name,gender):
	"""Positional argument in python function is refers to the
	position of the argument, value will be passed to the parameter
	based on it's position, e.g: a person name will be the first
	argument to pass to the function and the second one will be
	gender. If you pass gender first and name second then it will be
	stored in the wrong parameters, so the position of argument pass to
	the parameter is known as 'positional argument'. With order you
	will get an unexpected results"""


	print(f"\nHello! my name is: {name}")
	print(f"My gender is: {gender}")


#passing argument to function parameter sequentially
#first 'name' then 'gender'

#NOTE: You can call a function multiple times
id('Shinwari','male')
id('KFC','female')
id('Abbas','shemale')
id('imran','gay')