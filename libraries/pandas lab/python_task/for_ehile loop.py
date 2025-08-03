fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print("I like", fruit)
## by using while loops print 1 to 10 numbers
x = 1
while x <= 5:
    print("Count:", x)
    x += 1

i = 1
while i <= 10:
   print("number from 1 to 10 :",i)
   
   i += 1 
   
   
   # Example 1: for loop from 1 to 5
for i in range(1, 6):
    print("Number:", i)

# Example 2: Loop through list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print("I like", fruit)

# Example 3: while loop from 1 to 5
x = 1
while x <= 5:
    print("While loop count:", x)
    x += 1

# Example 4: Print even numbers between 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print("Even:", i)

# Example 5: Reverse a list using loop
colors = ["red", "blue", "green"]
for i in range(len(colors)-1, -1, -1):
    print("Reverse:", colors[i])
