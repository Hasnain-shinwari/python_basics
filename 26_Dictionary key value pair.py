#A dictionary in python is a collection of key pair value in a list
#element are enclosed in a {} brackets and key and pairs are seperated by comma
#at the end of each key are connected to it's value by colon

#this is an example of key and pair

benz = {'color': 'Black','model': 'S-Class'}

#accessing key pair values
print('Color of my Benz is: ',benz['color'])
print('\nModel of my Benz is: ',benz['model'])

#adding new key-pair values to dictionary
benz['Make']='Mercedes'
benz['Type']='AMG'

#accessing the new added elements from dictionary
print('\nMy car brand is: ',benz['Make'])
print('\nType of my car is: ',benz['Type'])

#Removing values/item from the dictionary
#a keyword 'del' has to be used to remove an item from dictionary

#remove color
del benz['color']

#remove Type
del benz['Type']

print('\nColor and Type items has been removed from the dictionary.')
print('\nThe following are the elements of dictionary now: ')
#accessing all elements through loop
for items in benz.items():
	print('\n\t',items)