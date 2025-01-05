# python follow by default calculation of numbers
# but you can specify the precedence
# Note that python will automaticaly handle the numbers of foalts, answer from division and exponent
# You can use underscore _ while writing a numbers that are easy to understand


first = 10
second= 20

#sumation
print('sum of two numbers:')
print(first+second)

#subtraction
print('\n\nsubtraction of two numbers:')
print(second-first)

#multiplication
print('\n\nmultiplication of two numbers:')
print(first*second)

#division
print('\n\ndivision of two numbers:')
print(second/first)

#exponent: In python exponent can be calculated as **
print('\n\nCalculating 3 power 3:')
print(3**3)


#order of precedence
print('\n\n Calculating 3 + 4 * 5')
print(3+4*5)

print('\n\nCalculating (3 + 4) * 5')
print((3+4)*5)

#underscore usage for better readability
underscore = 10_000_000
print('\n\nunderscore number:')
print(underscore)
