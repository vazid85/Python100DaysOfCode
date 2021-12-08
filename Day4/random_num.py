import random

num = random.randint(1, 10000)
print(f"My Random Number :: {num}")
if num % 2 == 0:
    print("Heads")
else:
    print("Tails")
