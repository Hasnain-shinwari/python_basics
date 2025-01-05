# sort is used for permanent change while sorted method is temporary
# len() will count the total number of items in the list
name = ['sunday','monday','tuesday','wednesday','tursday','friday']


# sorting temporary in accending order
print('\ntemporary sorted list:', sorted(name))


# sorting permanant in accending order
print('\n\npermanant sorted list:',name.sort())
print(name)

# sorting permanent in reverse order
name.sort(reverse=True)
print('\n\nsorting permananet in reverse order:',name)


# sorting  in reverse order
print('\n\nsorted list in reverse order:', name.reverse())
print(name)



# finding the length of the list using len() method
print('\n\nlength of the list is:',len(name))
