#10001st prime
#Problem 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?

import math

def primer(num):
    if num < 2:
        return False
    sqrt = int(math.sqrt(num))
    i = 2
    while i <= sqrt:
        if num%i == 0:
            return False
        i +=1
    return True

def problem7(num):
    isFound = False
    index = 0
    counter = 1
    while isFound != True:
        if primer(index) == True:
            counter += 1
        if counter > num:
            isFound = True
            return index
        index +=1
    #return index

print(problem7(10001))
