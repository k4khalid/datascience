#Exercise 1)i) - Using the following lists of cities
# per country
# Write a program that asks user to
# enter a city name and it should
# tell which country  the city belongs to

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Please enter a city name: ")
if city in india:
    print(city,"is in India!")
elif city in pakistan:
    print(city,"is in Pakistan!")
elif city in bangladesh:
    print(city,"is in Bangladesh")
else:
    print(f"With my current knowledge, I'm afraid I cannot tell you which country {city} is in")

#Exercise 1)ii) Write a program that asks user to enter
# two cities and it tells you if they both are in same country
# or not. For example if I enter mumbai and chennai, it will
# print "Both cities are in India" but if I enter mumbai
# and dhaka it should print "They don't belong to same country"

cities = input("Please enter two cities: ")
if cities in india:
    print("Both cities are in India")
elif cities in pakistan:
    print("Both cities are in Pakistan")
elif cities in bangladesh:
    print("Both cities are in Bangladesh")
elif cities in india or pakistan or bangladesh:
    print("They don't belong to the same country")
else:
    print("I don't have enough knowledge to say, sorry.")

#Exercise 2 - Write a python program that can tell you if your
# sugar is normal or not. Normal fasting level sugar range is 80
# to 100. Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high
# otherwise print that it is normal

sugar_level = input("Please enter your fasting sugar level: ")
sugar_level = int(sugar_level)
if sugar_level < 80:
    print("Sugar is low")
elif sugar_level > 100:
    print("Sugar is high")
else:
    print("Sugar is normal")