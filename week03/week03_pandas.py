import pandas as pd

df4 = pd.DataFrame({
    'date':['2025-09-11','2025-09-11','2025-09-12','2025-09-12'],
    'city':['서울', '안양', '서울', '안양'],
    'temp':[23, 22, 24, 26]},
    index=[1, 2, 3, 4]
)
# print(df4[['date', 'temp']])
# print(df4['temp'])
print(df4)
# print(df4.iloc[1:3])
# print(df4.iloc[:,[0,2]])
print(df4.iloc[1:3,[0,2]])