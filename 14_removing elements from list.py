#removing an item from a list have many approches


name = ['sunday','monday','tuesday','wednesday','tursday','friday']

# del: this method is usefull to remove an item by it's position or an index

# removing index 1 item monday

del name[1]

print('\n\nitem monday has been removed:')
print(name)


# pop: poping an item is similer to del but you can have this item. so it will remove the item from the end of the list and you can have it

pop_item = name.pop()
print('\n\npop item is:', pop_item)

# poping an element from any position you want
print('\n\nPop element at index 3:',name.pop(3))


# now removing an element from list by it's value
name.remove('sunday')
print('\n\nRemoving item from index 0:',name)
