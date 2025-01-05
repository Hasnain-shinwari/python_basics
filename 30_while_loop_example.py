#in this while loop example we will ask user to enter a promp
#and we will repeat the prompt until user enter quit

promt = "Enter a promt:"
promt += "I will repeat after you, until you 'quit':\t"

message = ""

while message !='quit':
	message = input(promt)
	if message !='quit':
		print(message)
