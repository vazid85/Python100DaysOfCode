
A=['11','12','13']
B=['21','22','22']
C=['31','32','33']

D=[A,B,C]
print(f"{A}\n{B}\n{C}")

position = input("position")

x = int(position[0])
y = int(position[1])

print(x-1)
print(y-1)

print(D[x-1][y-1])