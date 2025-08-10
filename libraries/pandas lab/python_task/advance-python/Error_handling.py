# Example 1: Basic try-except
try:
    num = int(input("Enter a number :"))
    print("you entered",num)
except:
     print("inavlid input!")
     
     # Example 2: Multiple except blocks
try:
    x = 10/0
except ZeroDivisionError:
       print("cannot divide by zero:")
except ValueError:
         print("wrong value entered!")

# Example 3: filles not found error
         
try:
    f = open("data,txt","r")  
    print(f.read())
except FileNotFoundError:
    print(" file not found")
else:
    print(
    "file print succrssfuly"
    )
finally:
    print("finally executions finished")
         
         

# Example 4: Handling specific error


try:   
    nums = [1, 2, 3]
    print(nums[3])
except IndexError:
    print("Index out of range!")

# Example 5: Combining multiple errors
try:
    a = int("abc")
except(ValueError,TypeError)  as e:
    print("error",e)

    