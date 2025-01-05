#Return value in python function

def return_val(fname='null',lname='null'):
	"""This function is taking two arguments first name and 
	last name and it will also return the combination of
	them"""

	full_name= f"{fname}  {lname}"

	#returning a full name to function call
	return full_name.upper()

#function calling 
combine = return_val('Hasnain','Shinwari')

#now printing combined names
print(combine)

