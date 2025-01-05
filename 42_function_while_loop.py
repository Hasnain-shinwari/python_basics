#python function with while loop 


def identity(fname,lname,mname=None):

	full_name=f"{fname} {lname}"

	return full_name.title()


while True:
	print('\nEnter your first and last name here')
	print('\nTo exit/quit at any time press q:')

	fname = input('\nPlease Enter your first name: ')
	if fname == 'q':
		break

	lname = input('\nPlease Enter your last name: ')
	if lname=='q':
		break

	combined = identity(fname,lname)
	print('Hello!  ', combined)