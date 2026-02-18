# Name : Clement Ngotho
# Date : 18/02/2026
# Program to show lists in python
# List of friends
friends = ["Rachel","Phoebe","Ross","Chandler","Monica","Joey"]

print(friends)
friends.sort()
print(friends)

friends.reverse()
print(friends)
friends.append("Jack")
print(friends)

new_friends = ["Tracy","James","Faith","Don","Augustine"]
print(len(new_friends))

#new list of students
students = friends + new_friends
print(students)

students.pop()
print(students)
students.insert(5,"Jenny")
print(students)

students.insert(8,"Vallary")
print(students)

students.extend("James")
print(students)

