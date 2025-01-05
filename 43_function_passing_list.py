#In this program we will pass a list to the function

#function defination
def capital(cars):
	"""we will read all the car names from a list using for loop
	then we will display each name in capital letter"""

	#for loop
	for car in cars:
		print('\n\t', car.upper())


#defining a list of car names
vehicals = ['benz','audi','bmw','vw','skoda']

#displaying only one line:
print('\n\t These are my favoirat Car Brands: ')
#function call 
capital(vehicals)