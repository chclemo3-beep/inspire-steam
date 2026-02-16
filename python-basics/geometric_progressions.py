# Name : Clement Ngotho
# Date : 13/02/2026
# Program calculate geometric progression

n = int(input("Enter number of terms"))
a = int(input("Enter the first term"))
r = int(input("Enter the common ratio"))

import math

Tn = a*(r**(n-1))
Sn = (a*(1-r**n))/(1-r)

print("The Nth term is:",Tn)
print("The sum of the terms is:"Sn)

