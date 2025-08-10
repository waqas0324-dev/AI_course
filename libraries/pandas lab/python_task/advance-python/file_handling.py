## file read method 
file = open("data.txt", "w")
file.write("\n Hello , this is my first files.\n")
file.write("\n. This is my first lines.\n")
file.close()


# files read method

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()


# files append

file =open("data.txt","a")
file.write("\n this is a apppend.\n")
print(content)
file.close()

 ## read lines by lines
file = open("data.txt","r")
for line in file:
     print(line.strip()) 
file.close()
    

    # Using with (auto close file)
with open("data.txt","r") as file:
     print(file.read())