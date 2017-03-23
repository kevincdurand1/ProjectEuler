"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
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

def problem10(maxvar = 2000000):
    sumvar = 0
    for i in range(0,maxvar+1):
        if primer(i) == True:
           sumvar +=i
    print(sumvar)
    return sumvar


problem10()
