#in this block of python code we will be discussing
#the arbitrary number of argument.
#means that a python function will accept arguments
#is much is user give there is no limit


#program for adding features in the car in pre-order

#function defination
def order(*features):
	"""The *features is known as an arbitrary function which
	will receive arguments in the function as user give. e.g
	7 arguments or 5 argument, each will be treated all the
	function call differently"""

	for feature in features:
		print(f"-- {feature}")


#function call: user 1 pre-order
print('\n\tUser 1: Car features on pre-order are: ')
user1 = order('Parking-sensors','Ridar','Panaromic roof','Cruies-control')

#function call: user 2 pre-order
print('\n\tUser 2: Car features on pre-order are: ')
user2 = order('Sports wheel','Spoiler','Adass-function')

