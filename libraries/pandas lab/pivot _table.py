
import pandas as pd

# 🔹 Sample data banate hain:
data = {
    'Department': ['Sales', 'Sales', 'HR', 'HR', 'IT', 'IT'],
    'Employee': ['Ali', 'Sara', 'Zara', 'Ahmed', 'Raza', 'Hina'],
    'Salary': [50000, 55000, 45000, 47000, 60000, 65000],
    'Bonus': [5000, 6000, 3000, 3500, 7000, 7500]
}

# 🔹 DataFrame banayein:
df = pd.DataFrame(data)
print("\n🔹 Original DataFrame:\n")
print(df)

# 🔸 Step 1: Pivot Table banaein - average salary per department
pivot1 = pd.pivot_table(df, values='Salary', index='Department', aggfunc='mean')
print("\n🔸 Average Salary by Department:\n", pivot1)

# 🔸 Step 2: Multiple values (Salary & Bonus), aggregation = sum
pivot2 = pd.pivot_table(df, values=['Salary', 'Bonus'], index='Department', aggfunc='sum')
print("\n🔸 Total Salary & Bonus by Department:\n", pivot2)
