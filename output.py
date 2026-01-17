#Cretae 3 variables to collect info from a user
#These variables are fist name, country and city
#print off their information ->ex John lives in Seatle, USA
#
#Create 2variables to gather user information
# 1 car rental price for 1 day 1 number of days to rent
#Create a total variable to multiply these 2 variables together
#print out their total cost

rental_price = input("Enter rental price per day: ")
rental_price = int(rental_price)
days = input("Number of days to rent: ")
days = int(days)

total = rental_price * days
print("The total cost to rent the car is:" ,total)

def add(a,b):
    return a + b
result = add(3, 5)
print(result)


def square(x):
     return x*x
result = square(3)
print(result)