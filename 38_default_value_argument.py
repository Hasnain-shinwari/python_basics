#in code we will discuss defualt value funcitons in python

#function defination
def default_val(name,spacail,field='Cyber Security'):
	"""In default value argument we set the fucntion parameter to
	a default value that we want, so if you skip the value it
	will print the default value assinged to the parameter, but
	you can modify it you keyvalue argument by usign the same
	parameter name is mentioned in the function defination"""

	print(f"\nMy name is :  {name}")
	print(f"I am a student of: {field}")
	print(f"My specaility is in: {spacail}")


default_val('Shinwari','Penetration Testing')
default_val('Abdullah','Java',field='Programming')
default_val('Imran','Flutter',field='Programming')
default_val('Abbas','Machine Learning',field='AI')

#NOTE: The default value parameter should be listed after all
#		the parameter that does not have default value		