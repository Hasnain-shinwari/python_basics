#in this programe we will
#remove an item from a list ethier repeated or not
#using while loop

list_1 = ['Benz','BMW','Audi','BMW']

print('\nitems before removing BMW: '+ str(list_1))

#using while loop
while 'BMW' in list_1:
	list_1.remove('BMW')

print('\nitems after remove BMW: ' + str(list_1))