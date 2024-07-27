# Ex 1) break = 5
# This code doesn't work because 'break' is a keyword and standalone statement within a loop
# it cannot have any values assigned to it

# Ex 2) code to calculate my age based off years
birth_year = 2005
current_year = 2024
age = current_year - birth_year
print(age)

# Ex 3) code to output my full name using different variables
forename = "Khalid"
middle_name = " Hashim Haroun "
surname = "Elrasheed"
full_name = forename + middle_name + surname
print("My full name is:", full_name)

'''
# Ex 4) Selecting the invalid variables names:
#_nation, 1record, record-one, record^one, continue

#_nation is valid - variable names can start with an underscore
# 1record is invalid - variable names cannot start with a digit. They must start with a letter (a-z, A-Z) or an underscore (_).
# record-one is invalid - This is an invalid variable name. Hyphens (dashes) are not allowed in Python variable names. The interpreter will interpret the hyphen as a minus sign, leading to a syntax error.
# record^one: This is an invalid variable name. The caret (^) symbol is not allowed in Python variable names. It is interpreted as the bitwise XOR operator in Python.
# continue: This is an invalid variable name. Continue is a reserved keyword in Python. Keywords cannot be used as variable names.
'''