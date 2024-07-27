#Exercise 1 - calculations using a list of expenses for each month
expenses = [2200,2350,2600,2130,2190]
#1)
print("I spent",expenses[1]-expenses[0], "dollars extra in February compared to January.")
#2)
print("My total expenses for the first quarter of the year was:", expenses[0]+expenses[1]+expenses[2], "dollars")
#3)
print("2000" in expenses)
#4)
expenses.append(1980)
print(expenses)
#5)
expenses[3] = expenses[3] - 200
print(expenses)

#Exercise 2 - manipulating a list of marvel super heroes
heroes=['spider man','thor','hulk','iron man','captain america']
#1)
print(len(heroes))
#2)
heroes.append("black panther")
print(heroes)
#3)
heroes.remove('black panther')
heroes.insert(3,'black panther')
print(heroes)
#4)
heroes.remove('thor')
heroes.remove('hulk')
heroes.insert(1,'doctor strange')
print(heroes)
#5)
print(dir(heroes))


