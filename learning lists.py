# Storing names of my friends in a list and printing one by one
friends = ['Afsar', 'Khalid', 'Hadil', 'Yasar', 'Zuhair', 'Imthiyas', 'Rizwan', 'Uwais']
for friend in friends:
    print(friend)

# Sending a greeting to them
for friend in friends:
    print(f"Hello {friend}, How are you?")

#creating a list and adding removing and replacing values from it   
cars = ['BMW', 'Audi', 'Ferrari', 'Bugatti' , 'Maruti']
#replacing maruti with maruti suzuki
cars[4]='Maruti Suzuki'
# Removing Maruti Suzuki because its engine is low power
removed_cars = cars.pop()
#Adding Mclaren 
cars.append('Mclareen')

#Learning to sort the list using sorted, reverse and sort
print('The original cars list')
print(cars)
print("\n The car that has been removed" )
print(removed_cars)
print(f"THe cars sorted temporarily \n{sorted(cars)}")
print(f"The original list remains unchanged \n{cars}")
print("reversing the original list")
cars.reverse()
print(cars)
print("Permenantly making the list in alphabetical order")
cars.sort()
print(cars)