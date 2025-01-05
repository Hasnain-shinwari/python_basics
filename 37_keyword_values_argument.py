#keyword value argument function in python

#function defination
#about favorait car
def f_car(name,model):
	"""keyword value argument in python functions is refers to
	the function which a user will pass the argument to parameter
	using the same name defined in function defination(parameter)
	. This will prevent you from an unexpected errors in ordering
	of argument"""
	print('\nThis is the car that I like the most:')
	print(f"Name of the car is: {name}")
	print(f"Model of the car is: {model}")



#passing argument as a keyvalue argument to the function
#without order
f_car(name='Mercedes-Benz',model='S Class')
f_car(model='7 Series', name='BMW')
