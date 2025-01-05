#for more than two condition python has if-elif-else which only one of these will be checked

#code to check whether you are eligible or not for driving test

age = 70

if age ==18 or age <= 60:
	print('\nDear you are eligible for the test:')
elif age < 18:
	print('\n\nYou are under age, NOT ELIGIBLE:')
else:
	print('\n\nYou are too old please dig a grave for yourself:')
