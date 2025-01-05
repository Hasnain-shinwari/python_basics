# In this code we will remove white spaces from strings and variables

message = 'python   '

#remove right strips
message = message.rstrip()
print(message)

#remove left strips
message = message.lstrip()
print(message)

#removing both side strips/whitespace
message = message.strip()
print(message)