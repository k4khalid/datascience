# Exercise 1 - After flipping a coin 10 times you got this result:
# Using for loop figure out how many times you got heads

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
for i in result:
    if i != "heads":
        i = i+1

print(i)
