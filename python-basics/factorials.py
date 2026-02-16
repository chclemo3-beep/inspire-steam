#Clement Ngotho
#16/2/2026
#Program to calculate the factorials of numbers

number = int(input("Enter the number x :"))
factorial = 1 #intialise the factorial to 1

for x in range (1,number + 1):
    factorial = factorial * x

print(f"{number}!={factorial}")