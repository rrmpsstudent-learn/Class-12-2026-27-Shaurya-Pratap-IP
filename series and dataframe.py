import pandas as pd
import numpy as nm

d1 = {'Roll No': 1, 'Name': 'Ram', 'Marks': 20}
d2 = {'Roll No': 2, 'Name': 'Ravi', 'Marks': 18}
d3 = {'Roll No': 3, 'Name': 'Rakesh', 'Marks': 13}
d4 = {'Roll No': 4, 'Name': 'Ramu', 'Marks': 8}
d5 = {'Roll No': 5, 'Name': 'Ramesh', 'Marks': 19}
d6 = {'Roll No': [1,2,3,4,5], 'Name': ['Ram', 'Ravi', 'Rakesh', 'Ramu', 'Ramesh'], 'Marks': [20, 18, 13, 8, 19]}

df1 = pd.DataFrame([d1, d2, d3, d4, d5])
df2 = pd.DataFrame(d6)
df3 = pd.DataFrame([{'Roll No': 1, 'Name': 'Ram', 'Marks': 20}, {'Roll No': 2, 'Name': 'Ravi', 'Marks': 18}, {'Roll No': 3, 'Name': 'Rakesh', 'Marks': 13}, {'Roll No': 4, 'Name': 'Ramu', 'Marks': 8}, {'Roll No': 5, 'Name': 'Ramesh', 'Marks': 19}])

arr1 = nm.array([1,2,3,4,True,False])
l1 = [1,2,3,"Arjun",29.1,True]

print(df1)
print("-------x-------")
print(df2)
print("-------x-------")
print(df3)