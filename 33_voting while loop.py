#in this program we will ask user to vote
#using user input in python and while loop
#the result will be stored in dictionary

dictionary = {}

#seting flag to true
flag = True

#while loop
while flag:
	#asking user name and voter name
	name = input('\nEnter your name dear: ')
	vote = input('\nWrite voter name please: ')

	#storing results dictionary
	dictionary[name] = vote

	#checking if anyone else is want to vote?
	repeat = input('\nIs there anyone else to vote(yes/no): ')
	if repeat == 'no':
		flag = False

#displaying voting from the dictionary using items()
print('\n\t Voting complate here are the result:')
for name,vote in dictionary.items():
	print(f"{name.title()} he voted to {vote.title()}:")

