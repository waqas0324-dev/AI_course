# 1 to 10 tak number print kry 
i = 1
while i <= 10:
    print("numbers:", i)
    i += 1
    
    ## 5 yo 1 reverse numbers
i = 5 
while i >= 1:
    print("Numbers is :", i)
    i -= 1
    
    # Example 4: break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# Example 5: continue statement
for i in range(5):
    if i == 2:
        continue
    print(i)
   
    
    # list using loops 
fruits = ["apple","banana","orange","pineapple"]
for fruit in fruits:
    print("fruit:", fruit)
    # Urdu: Phalon ka list banayein aur har fruit ko print karein
# English: Create a list of fruits and print each one



    
    ## even numbers 
    
for i in range(1,21):
    if i % 2 == 0:
        print("even numbers:", i)
        
        # reverse list itme using loops 
colors = ["red", "green", "blue", "yellow", "black"]
for i in range(len(colors) -1, -1, -1):
    print("color:", colors[i])