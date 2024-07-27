# Exercise 1 - code to calculate the total area of a football field, rounded to 2dp
field_length = 92
field_width = 48.8
field_area = field_length * field_width
print(round(field_area,2))

# Exercise 2 - code to work out the change from shopping
potato_chips = 1.49
spent = potato_chips * 9
paid = 20
change = paid - spent
print("The shopkeeper is going to give me : $",change,sep="")

#Exercise 3 - code to work out the total cost of tiles in a bathroom
square_length = 5.5
square_area = 5.5**2
total_cost = round(500 * square_area)
print("The total cost to replace all tiles is: $",total_cost,sep="")

#Exercise 4 - code to print the binary representation of the number 17
# number = 17
# remainder = number % 2
num=17
print('Binary of number 17 is:',format(num,'b'))
# The format function can be used to convert numbers to different formats including binary, decimal, hexadecimal and octal