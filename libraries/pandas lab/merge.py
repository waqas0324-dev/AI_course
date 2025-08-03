import pandas as pd
# 🔹 DataFrame 1: Student basic info
student1 = pd.DataFrame({
    'students_id': [101,102,103,104],
    'Name': ["waqas","Ali","Ahmad","Areeba"]
})


student2 = pd.DataFrame({
    'students_id':[101,102,103,104],
    'Marks': [90,80,85,75]
})
df = pd.DataFrame(student1)
df = pd.DataFrame(student2)

print("both students results:\n")

print(df)

# start merge a data 

merge1 = pd.merge( student1,student2, on='students_id' , how= "inner")
print("\n Both tables are merged:\n" , merge1)