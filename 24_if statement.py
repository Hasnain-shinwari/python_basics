#if statment will check the condition according to the rules you give


car ='benz'
#checking car if it is equals to benz
print('\ncheck car if it is equals to "benz":')

#if condition using loop
if car=='benz':
	print('\nresult matches with "benz":',car)
else:
	print('\nresult not matched with "benz":')

#same condition but checking for non equality
print('\n\nLooking for car name toyota:')

if car!='toyota':
	print('\n\n does not matches')
else:
	print('\n\nmatches the result')


#burger list
burgers=['zinger','chicken steak','grilled']

print('\n\nThis is the burger list:',burgers[:])

#checking if the burgers are in the list 
print('\nCheck burger zinger if it is in the list: ','zinger' in burgers)

print('\nCheck burger which is not in the list: ','mayo_burger' in burgers)

