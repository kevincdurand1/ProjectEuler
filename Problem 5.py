#Smallest multiple
#Problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def problem5(num):
    mod = 0
    start = 1
    found = False
    while (found != True):
        for i in range(1,num+1):
            mod += (start%i)
        if mod != 0:
            start = start + 1
            mod = 0
        else:
            found = True
    return start

print(problem5(20))