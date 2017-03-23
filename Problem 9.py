'''
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def problem9():
    val = 0
    isfound = False
    while isfound == False:
        for a in range(1, 1001):
            for b in range(1, 1001):
                if b > a:
                    continue
                for c in range(1, 1001):
                    if c < b:
                        continue
                    if a + b + c == 1000 and a**2 + b**2 == c**2:
                        val = a * b * c
                        isfound = True
        return print(val)


problem9()
