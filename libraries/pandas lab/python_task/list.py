fruits = ["apple", "banana", "mango"]
print(fruits)
print(fruits[0])  # First item
print(len(fruits))  # Kitne items hain
fruits.append("orange")     # List mein add kare
fruits.remove("banana")     # Kisi item ko hataaye
print("mango" in fruits)    # Check if exists
print('apple'in fruits)
## 5 exampels 
# Example 1: Simple list
names = ["Ali", "Sara", "Ahmed"]
print(names)

# Example 2: Access specific item
print("Second name is:", names[1])  # Indexing 0 se start hoti hai

# Example 3: Add item in list
names.append("Zara")
print("After adding:", names)

# Example 4: Remove item
names.remove("Ahmed")
print("After removing:", names)

# Example 5: Check if item exists
if "Sara" in names:
    print("Sara is in the list")

## advanced list method 
# .format()
name = "Waqas"
age = "21"
print("students  is {} age {} years old ".format(name, age))

# .join 
words = ["Waqas", "sagar","love"]
sentence = " ". join(words)
print(sentence)

# . split
text = "apple,banana,mango"
fruits = text.split(' ,')
print(fruits)