# Name : Clement Ngotho
# Date : 23/02/2026
# Program to show inheritance in python docs

class Animal():

    def __init__(self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self,weight):
        weight = 1.1 * weight
        print("The animal weighs {weight} in kgs")

    def eat(self,food):
        print("The animal eats {food}")