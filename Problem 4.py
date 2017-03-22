#Largest palindrome product
#Problem 4
#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#Limits are from 100 to 999
#need to perform multiples of combinations of i x j
#Determine if product is palindromic #
#If Palindromic add to list
#find max of list

def isPalindrome(num):
    return str(num) == str(num)[::-1]

target =  0
for i in range(100,1000):
    for j in range(100,1000):
        if isPalindrome(i * j) and (i * j) > target:
            target = i * j
print(target)