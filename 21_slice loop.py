#Using loop through slice

values=['benz','audi','bmw','vw','ford','lexus']

#using loop to access all elements of the list
print('\n\nLooping all the elements in list:')
for x in values[:]:
	print(x)

#printing first three elements using loop
print('\n\nprinting first three elements in uppercase using loop:')
for value in values[:3]:
	print(value.upper())

#printing last three elements using loop
print('\n\nprinting last three elements in lowercase using loop:')
for a in values[:-3]:
	print(a.lower())



#printing 