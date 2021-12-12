

numbers_list = [3,4,6,2,10,30,34,43,5,44,66,75,33]
num = int(input("Please enter the element to search"))
print(num)
i=0
for element in numbers_list:

    if element == num:
        print(element)
    else:
        print(f"{num} not found in the list")
        continue

