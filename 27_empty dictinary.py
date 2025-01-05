#starting with an empty dictionary
#then adding values if needed

#an empty dictionary should be start with two curly brackets
car_colors = {}

#adding colors of the cars and price
car_colors['Black'] = '$1000'
car_colors['White'] = '$900'
car_colors['Metalic Gray'] = '$1500'
car_colors['Armeld Green'] = '$2500'

#now accessing car colors keys with keys() option
print('\nAccessing elements with keys() option:')
print('Paints we are offering are:')

# using for loop to access it using key
for key in car_colors.keys():
	print('\n\t',key)

# now accessing car colors cost for each paint with values() option
print('\nAccessing elements values with values() option')
print('Cost of each color/paint is:')

#using for loop to access dictionary values
for val in car_colors.values():
	print('\n\t',val)

#now combinnig the keys and values to print using items() option
print('\nAccessing items of the dictionary using items():')
print('These are the colors/paints and cost of each is:')

#using for loop to access dictionary element with items() option
for item in car_colors.items():
	print('\n\t',item)