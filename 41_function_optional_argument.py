#in this code we will discuss an optional argument value

#asking users to enter your fisrt and last names as well as middle(optional)
print('\nEnter your first, middle(optional), and last name: ')

#defination of the funcition
def full_n(fname,lname,mname=''):
	"""we will ask user to enter you first, middle and last name 
	but if he did not entered middle name we will print only
	first and last in full name. Now the middle name is optional"""

	#combining names
	if mname:
		full_name = f"{fname} {mname} {lname}"

	else:
		full_name = f"{fname}  {lname}"

	return full_name.upper()

comb = full_n('hasnain','khan','shinwari')
print(comb)

comb = full_n('hasnain','shinwari')
print(comb)