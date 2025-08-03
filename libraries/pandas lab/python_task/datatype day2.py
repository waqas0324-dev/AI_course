### datatype 
age = 18        # int
price = 99.99   # float
name = "Ali"    # str
is_adult = True # bool

print(age,(type(age)) )     # Output: <class 'int'>
print(type(name))     # Output: <class 'str'>
print(type(is_adult))
print(type(price))

# Example 1: Integer
age = 25
print("Age:", age, "Type:", type(age))

# Example 2: Float
price = 99.50
print("Price:", price, "Type:", type(price))

# Example 3: String
name = "Ayesha"
print("Name:", name, "Type:", type(name))

# Example 4: Boolean
is_passed = True
print("Passed:", is_passed, "Type:", type(is_passed))

# Example 5: Mixing all
print(name, "is", age, "years old. Fee is", price, "and passed:", is_passed)




##input type 
name = input("Enter your name: ")
print("Welcome,", name)
age = int(input("Enter your age :"))
print("I am ", age ,"year old")

# Example 1: Get name
name = input("Enter your name: ")
print("Welcome", name)

# Example 2: Get age as number
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Example 3: Add two numbers from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum is:", a + b)

# Example 4: Get float values
price = float(input("Enter price: "))
discount = float(input("Enter discount: "))
print("Final Price:", price - discount)

# Example 5: Full name using two inputs
first = input("Enter first name: ")
last = input("Enter last name: ")
print("Full name:", first + " " + last)
