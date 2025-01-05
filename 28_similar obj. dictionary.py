#a dictionary in python can be of a similar objects
#if you students that what are the most famous car brands

car_brands ={
	'shinwari':'benz',
	'abdullah':'nissan',
	'abbas':'bmw',
	'hassan':'honda',
	'imran':'toyota',
	'hamid':'honda',
	'uziar':'toyota',
	'zaid':'honda',
}

print('Each student has their faveriot car brand:')
#accessing element of each student using loop
for brands in car_brands.items():
	print('\n\t',brands)

print('\nShinwari faveriot car brand is:',car_brands['shinwari'])

#accessing elements using get() command because simple accessing
#will cause an error if the element key-pair value is not in the dic.
#so to handle this kind of error we will use get, get will take two arguments
#first will be the key and second will the message to display in the apsence of value


#displaying value that is not present in the dictionary: color or type
print('Color of my car is: ',car_brands.get('color','sorry value does not exist'))

#using get without second argument it will return none only
print('\nType of my car is:', car_brands.get('Type'))