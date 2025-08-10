# Example 1: Create a list of numbers
nums = [x for x in range(5)]
print(nums)  # [0, 1, 2, 3, 4]

# Example 2: Square of numbers
squares = [x**2 for x in range(5)]
print(squares)

# Example 3: Even numbers only
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Example 4: Convert to uppercase
names = ["ali", "ahmed", "umar"]
upper_names = [name.upper() for name in names]
print(upper_names)

# Example 5: Filter strings with length > 3
words = ["hi", "hello", "yes", "no", "python"]
long_words = [w for w in words if len(w) > 3]
print(long_words)
