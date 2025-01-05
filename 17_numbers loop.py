#In this code we will look it the digits or numbers to print using loop

#print numbers form 0 to 10

print('\n\tThese are the values from 1 to 10:')
for i in range(1,11):
	print(i)


#printing values in the list

values=list(range(10,21))

print('\n\tRange has been used in the list to print NO. from 10-20:')
print(values)


#finding squares of no. from 1-10 in a list

squares=[]
for square in range(1,11):
	squares.append(square**2)

print('\n\tsquares from 1-11:')
print(squares)