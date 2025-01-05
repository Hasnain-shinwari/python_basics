#in this lines of code we will pass an
#argument to the function salam

print('This is the argument function:')

#declaring function
def salam(name):
	"""The 'name' in salam() function header is known as parameter
	a parameter will store the argument, while an argument is 
	something that pass to the function salam() and store in
	the parameter 'name', here the argument is 'shinwari' which
	is passed to function as a string. NOTE: do not use argument
	and parameter interchangably they are different things."""
	
	print(f"Asalam-O-alaikom, {name.title()}")


#calling functin salam
salam('shinwari')