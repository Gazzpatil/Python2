#using for loop

'''number = int(input("enter the number:"))
i=1
for i in range(1,11):
    print(i*number)'''

'''The current population of a town is 10000. The population of the town is increased at the rate of 10% per year.You have to write a program to find out the population at the end of each of the last 10 years.'''

current_pop = 10000
for i in range(10,0,-1):
    print(i,current_pop)

    current_pop=current_pop - (0.1*current_pop)
print(current_pop)