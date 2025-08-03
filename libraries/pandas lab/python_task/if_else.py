# Example 1: Voting age check
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote.")
else:
    print("You are not eligible.")

# Example 2: Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Example 3: Pass/Fail
marks = int(input("Enter marks: "))
if marks >= 40:
    print("You passed")
else:
    print("You failed")

# Example 4: Positive or Negative
n = int(input("Enter any number: "))
if n > 0:
    print("Positive")
else:
    print("Negative or Zero")

# Example 5: Password check
password = input("Enter password: ")
if password == "admin123":
    print("Access granted")
else:
    print("Wrong password")
