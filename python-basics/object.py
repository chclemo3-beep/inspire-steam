# Name : Clement Ngotho
# Date : 19/02/2026
# classes (objects) in python

class human:
    # First we define the attributes of a human being
    type = "Mammal"
    legs = 2
    brain = True
    warm_blooded = True
    city = "Nairobi"

    # We the create a constuctor for the class/object
    # The constructor will be used to create copies
    def __init__(self, name, age):
        self.human_name = name
        self.human_age = age

    def tell_story(self):
        print(f"Hello, I am{self.human_name} Here is a story")
        print("There was once a bot that said hello world")

#Create the humans
amani = human("Amani",17)
triza = human("Triza",17)

#Let the human created do things
amani.tell_story()
print("Amani's age is: ",amani.human_age)

# Modify one of the objects without modifying other objects
triza.city = "Kiambu"

print("Triza's location is", triza.city)
print("Amani's location is" , amani.city)

