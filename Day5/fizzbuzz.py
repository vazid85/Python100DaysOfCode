#This program will display values which devided by 3 or 5out of 100 integers including 100

#Create List

numbers = range(1, 101)
for i in numbers:
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%5==0:
        print("buzz")
    elif i%3==0:
        print("fizz")
    else:
        print(i)