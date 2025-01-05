#elements in a list that can not be changed are known as immutable by python and an immutable list is knows as tuple
#tuple: is a list of values which can't be changed through out the whole program

# tuple are elements inclosed in a parenthesis brackets which are easy and simple also increase the program readablity

#stick has only length and width
sticks =(222,444)

#looping to access the elements of a tuple
print('\n\nlooping values through the loop:')
for stick in sticks:
	print(stick)

#tuple with only one value should be wirten as below: value will be seperated with comma

one=(2,)
print('\n\ntuple of one value (2,):',one[0])


#modifying the tuple values:
#the variable should be same as above without that you can not modify it

sticks=(333,555)
print('\n\nmodified values of tuple:')

# accessing through the loop
for stick in sticks:
	print(stick)

