import threading
import math


def countEven(numbers):
    counter = 0
    for number in numbers:
        if int(number) % 2 != 0:
            counter += 1
    print(f"{counter} Even number")

def countOdd(numbers):
    counter = 0
    for number in numbers:
        if int(number) % 2 == 0:
            counter += 1
    print(f"{counter} Odd number")


print("this list contian:")
numbers = [9, 2, 7, 3, 8, 1, 3,4,7,6,4,3,2,1,1,1,3,3,4,5,9,9,8,8,7,9]

x = threading.Thread(target=countOdd, args=(numbers,))
x.start()

y = threading.Thread(target=countEven, args=(numbers,))
y.start()







