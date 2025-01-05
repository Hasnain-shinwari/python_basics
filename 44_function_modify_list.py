#in block of python code we will be discussing 
#pssing list to a function and modifying it

#program to printing car brands name that are safe
print('\n\tChecking car safty here:\n')
#list of cars
cars_list=['benz','audi','vw','lexus','bmw']

#here the safe cars will be stored
safe_cars=[]

#function to check for safety
def safe(cars_list,safe_cars):
	while cars_list:
		safe = cars_list.pop()
		print(f"This {safe.upper()} has been checked for safty")
		safe_cars.append(safe)

#function to display the safe cars
def disp_safe_cars(safe_cars):
	for safe_car in safe_cars:
		print(f"{safe_car.upper()} is a safe car")

#function call
safe(cars_list,safe_cars)

#displaying safe cars
print('\n\tThese are the safe cars to drive:\n')
disp_safe_cars(safe_cars)