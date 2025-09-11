import pandas as pd

df4 = pd.DataFrame({
    'date':['2025-09-11','2025-09-11','2025-09-12','2025-09-12'],
    'city':['서울', '안양', '서울', '안양'],
    'temp':[23, 22, 24, 26]},
    index=[1, 2, 3, 4]
)
print(df4)
df9 = df4.sample(n=2)  # Randomly select n rows.
# print(df9)
# df10 = df4.nsmallest(2, 'temp')
df10 = df4.nlargest(2, 'temp')
# print(df10)
print(df4.head(3))
