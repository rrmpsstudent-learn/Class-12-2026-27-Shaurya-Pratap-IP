import pandas as pd
d1 = {"S1":pd.Series([1,2,3,4]), "S2":pd.Series([6,7,8,9]), "S3":pd.Series([11,12,13,14])}
df1 = pd.DataFrame(d1, columns=["S1","S2","S3"])
print(df1)