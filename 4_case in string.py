# in this code we will change the case of a string

message = 'python programming'
print('simple message')
print(message)

# changing string case to title
print('\n\nTitled string')
print(message.title())

# changing message to uppercase letters
print('\n\nUpperCase string')
print(message.upper())

# Now changing it to the lowercase
print('\n\nLowerCase string')
print(message.lower())

# to count all characters
print('\n\nCount character p')
print(message.count('p'))

# to replace the characters
print('\n\nReplaceing character g with G')
print(message.replace("g",'G'))

# to find a character m, counting will start with 0
print('\n\nFinding a character m')
print(message.find('m'))

# string conversion
print('\n\nString conversion')
message = str(123456789)
print(message)
