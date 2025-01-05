# in this program we will move item of one
# list to another an empty list

list_1 = ['Benz','BWM','Audi']
list_2 = []

# verify users from list 1 and then move to list 2
while list_1:
	current_user = list_1.pop()
	print(f"verifying user: {current_user}")
	list_2.append(current_user)


# now  displaying all information of list 2
print('\n\tThese are the items in list_2: ')
for items in list_2:
	print(items)