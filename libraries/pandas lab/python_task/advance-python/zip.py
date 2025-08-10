name = ["waqas","waso","ali"]
age = [20,21,12]

combined = zip(name,age)
print(list(combined))

#Eample 2:Zip with unequal lengths
a =[1,2,3,4,5]
b=['x','y','z','w']
z= zip(a,b)
print(list(z))