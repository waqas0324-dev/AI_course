### function method 

def greet():
    print("Hello welcome waqas to Ai:")

greet()

# Example 2: Function with 1 argument
def welcome(name):
    print("welcome", name)

welcome("waqas")

# Example 3: Function with 2 arguments

def add_fuc(a,b):
    print("sum = ", a+b)

    print("multiply = ", a*b)

add_fuc(8,9)

# Example 4: Function with return value
def multiply(x,y):
    return x*y
   
results =multiply(9,8)

print("multiplications:",multiply)

# Example 5: Check even or odd
def check_even(numbers):
    if numbers %2 == 0:
        print("Even numbers:",numbers)
    else:
        print("ODD numbers:",numbers)

check_even(9)
check_even(8)