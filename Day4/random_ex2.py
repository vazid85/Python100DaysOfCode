import random

name_string = "Angela, Ben, Jenny, Michael, Chloe"

print(name_string)

names = name_string.split(',')

#get random number
i = random.randint(0, len(names)-1)
print(i)

print(f"{names[i]} is going to buy the meal today!")

