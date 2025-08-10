# Example 1: Addition

add = lambda x,y: x+y
print(add(3,7))

# Example 2: Check even or odd

even = lambda x: x %2 == 0
print(even(5))

# Example 3: Maximum of two numbers

maximum = lambda x,y: x if x > y else y
print(maximum(6,7))

# Example 4: Square root (approximate)
sqrt = lambda x: x*0.4
print(sqrt(5))

# Example 5: Reverse a string
reverse = lambda x: x[:: -1]
print(reverse("waqas"))

#2️⃣ Map Function – 5 Examples

numbers = [1,2,3,4,5,6]

# Example 1: cube of  each number
cube = list(map(lambda x: x**3 , numbers))
print(cube)

# Example 2: Convert to string

string = list(map(str, numbers))
print(string)

# Example 3: Add 10 to each number
sub_10 = list(map(lambda x : x-10 , numbers))
print(sub_10)

# Example 4: Boolean: check even / odd
odd_check = list(map(lambda x : x % 2 !=0 ,numbers))
print(odd_check)

# Example 5: Capitalize names

name = ["waqas","ahmad","waso"]
capitalized = list(map(lambda x: x.capitalize(), name))
print(capitalized)


##3️⃣ Filter Function – 5 Examples

numbers = [5, 12, 17, 18, 24, 32]

# Example 1: Filter numbers > 15

filter_num = list(filter(lambda x : x > 15,numbers))
print("\n Filter function exampels is print here:\n")
print(filter_num)

# Example 2: Filter even numbers

even_num= list(filter(lambda x : x%2 == 0 , numbers))
odd_num= list(filter(lambda x : x%2 != 0 , numbers))
print(odd_num)
print(even_num)

# Example 3: Filter strings starting with 'a'

name = ["waqas","ahmad","waso","ali"]
a_name = list(filter(lambda x: x.startswith('a'), name))
print(a_name)

# Example 4: Filter words with length > 4
words = ['cat', 'elephant', 'dog', 'lion']
filter_length = list(filter(lambda x: len(x) >= 4 , words))
print(filter_length)

# Example 5: Filter non-empty strings
strings = ['hello', '', 'python', '', 'AI']
non_empty = list(filter(lambda x: x != '' , strings))
print(non_empty)


#4️⃣ Reduce Function – 5 Examples

from  functools import reduce


numbers = [1, 2, 3, 4, 5]

# Example 1: Sum of all numbers
sum_all = reduce(lambda x, y: x+y , numbers)
print("\n Reduce function exampels is here:\n")
print(sum_all)

# Example 2: Product of all numbers

pro_num = reduce(lambda x,y : x*y, numbers)
print(pro_num)

# Example 3: Maximum number
maximum_num = reduce(lambda x,y: x if x>y else y , numbers)
print(maximum_num)

# Example 4: Minimum number
minimum_num = reduce(lambda x,y: x if x<y else y , numbers)
print(minimum_num)

# Example 5: Concatenate strings 
word = ['Hello', ' ' , 'waqas', '! ']
sentence = reduce(lambda x,y : x+y , word)
print(sentence)


