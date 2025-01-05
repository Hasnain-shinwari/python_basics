#a list can be copied without a loop using slice

#this is mine list of my favorite cars
mine_list=['benz','bmw','porche','audi']

#printing mine list of cars companies
print('\n\nThese are my favorite car brands:')
print(mine_list[:])

#my friend also like the car barands that i like
#so we will copy mine list to friend list

frnd_list=mine_list[:]

#printing frnd list 
print('\n\nThese cars brands are liked by my friend:')
print(frnd_list[:])


#i have liked another car brands lexus
mine_list.append('lexus')

print('\n\nI have add an another car brand to mine list:')
print(mine_list[:])


# my friend also have new brand that he liked suzuki

frnd_list.append('suzuki')
print('\n\nNew car brands has been add to my friend list:')
print(frnd_list[:])
