import random
names = input("Enter the names of the persons who will spilt teh bill: ").split(" ")

# print(names)

person_who_will_pay = random.choice(names) #selecting a person randomly from the  list

print(f"the bill will be paided by: {person_who_will_pay}")