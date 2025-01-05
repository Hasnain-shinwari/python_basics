# slice in python is used for to play with a specific elements fo list

numbers =list(range(1,11))
print('\nThese are the numbers of a list:')
print(numbers)

#print first 3 no.
print('\n\nprinting first three numbers:')
print(numbers[0:3])

#print no. from 4 to 8
print('\n\nprint numbers from 4-8:')
print(numbers[3:8])

#skip first three no. and dispaly the rest
print('\n\nskip first three no. and display the rest:')
print(numbers[3:])

#print last three numbers
print('\n\nprinting last three numbers:')
print(numbers[-3:])

#print all numbers from the start
print('\n\nprinting all numbers from start:')
print(numbers[0:])

#printing all numbers in reverse order
print('\n\nDisplaying numbers in reverse order:')
print(numbers[:])