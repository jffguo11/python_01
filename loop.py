import math

abc = [3, 34, 78.33, 234, 5]

deg = [3251, 1345, 68, 132509]

hij = ["captain", "super", "wonder", "iron"]

for x in abc:
    if x >= 50:
        print x
    else:
        print(str(x) + " " + "is not greater than or equal to 50")
#-----------------------------------------------------------

def counter(topv):
    for x in range(1,(topv + 1)):
        print x

counter(5)
#-----------------------------------------------------------

def findevens(lyst):
    for x in lyst:
        if x % 2 == 0:
            print(str(x) + " is even")

lyst1 = [32, 57, 94, 1008, 761]
findevens(lyst1)
#-----------------------------------------------------------

arr1 = [1, 42, 56, 71, 39, 55, 901]
arr2 = [2,1,4,65,776,79,321]
arr3 = arr1 + arr2
print arr3

def separr(lyst):
    """takes in an array and loops through each element
       if the element is even or equal to 1, say that the element is even or equal to one
       else(if the element is odd), say the element is odd """
    for x in lyst:
        if x % 2 == 0 or x == 1:
            print(str(x) + " is even or equal to one")
        elif x % 2 == 1:
            print(str(x) + " is odd and not equal to one")
separr(arr3)

#-----------------------------------------------------------

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(7))





