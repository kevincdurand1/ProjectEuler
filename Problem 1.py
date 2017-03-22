#Multiples of 3 and 5
#Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
import time


def problem1(x):
    total = 0
    for i in range(0, x ):
        if (i%3 == 0 or i%5 == 0):
            total += i
    return total

tStart = time.time()
print(problem1(1000))
print ("run time = " + str((time.time() - tStart)))
