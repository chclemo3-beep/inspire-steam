# Name : Clement Ngotho
# Date : 18/02/2026
# Program to define functions 

def cook_egg():
    oil = "20ml"
    pan = True
    moto = True
    eggs = 3

    print(f"The pan is {pan}, and the fire is {moto}, and {oil} amount of oil and cook {eggs} eggs")

cook_egg()  
print("Here is statement 1")

print("Here is statement 2")

cook_egg()

print("Here is statement 3")

#Ride fare creating function

def create_fare(route, distance, is_rush_hour):
    fare = distance * 10
    if is_rush_hour == True:
        fare = fare *1.5
    print(f"Your fare to {route} is {fare}")

    return fare

rush_hour = True
returned_fare = create_fare("Juja-Allsops",7,rush_hour)
print(f"The fare returned is {returned_fare}")
create_fare("Juja-Allsops",7,rush_hour)    

#Passing a list as a parameter
def write_all_interests(interests):
    for interests in interests:
        print(f"I am interested in {interests}")

all_interests = ["Swimming", "Hiking", "Working"]

write_all_interests(all_interests)

