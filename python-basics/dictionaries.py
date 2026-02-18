# Name : Clement Ngotho
# Date : 18/02/2026
# Program to show dictionaries in python

cars = {"Model" : "Audi","Make" : "Q8","Colour" : "Cherry","Year" : "2025"}
print(cars)

print(cars["Model"])
print(cars["Year"])

students = dict(Alice = 24,
                James = 18,
                Mark = 22,
                Daisy = 19)
for key in students:
    print(key)

for val in students:
    print(val)
