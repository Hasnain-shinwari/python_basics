#All in one about functions in python
#1 passing argument
#2 default value argument
#3 keyvalue argument


#function defination
def pizza(type,crust='pan toasted'):

	print('\n\tPizza Order Information:')
	print('Pizza Type:',str(type))
	print('Crust: ', str(crust))

#1
pizza('Small pizza','Hand Toasted')

#2
pizza('Large pizza')

#3
pizza(type='Medium Pizza',crust='Thin crust')
