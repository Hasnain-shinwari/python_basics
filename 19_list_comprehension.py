#list comprehension, is a usefull method to use in python
#it will allow you to create a same list in one line of code
#comprehension take expression first and then loop withou colon but all enclosed in a squared bracket same as list

#code to find out the squares of each number from 1-10

squares=[value**2 for value in range(1,11)]

#dispalying the numbers square
print('\n\tSquares of numbers from 1-10 are:\n')
print('\t',squares)