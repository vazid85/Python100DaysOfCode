import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
numbers=[0,1,2,3,4,5,6,7,8,9]
symbols =['?','/','^','@','$','#','&']

num_letters=input("Please enter character length")
num_numbers=str(input("Please enter numbers length"))
num_symbols=input("Please enter symbol length")

alfaChar=[]
for i in range(1,int(num_letters)+1):
    alfaChar.append(random.choice(letters))

for i in range(1,int(num_numbers)+1):
    alfaChar.append(random.choice(numbers))

for i in range(1,int(num_symbols)+1):
    alfaChar.append(random.choice(symbols))
random.shuffle(alfaChar)

pwd=''
for i in alfaChar:
    pwd += str(i)

print(pwd)
