#Example 1: Loop me index ke saath use
fruits = ["Apple","Mangoes","Banana","Cherry"]
for i , fruit in enumerate(fruits):
    print(i,fruit)
    
    
    #Example 2: Starting index change karna
for i ,fruit in enumerate(fruits , start=1):
    print(f"index {i}: {fruit}")