import pandas as pd

df4 = pd.DataFrame({
    # 'date':['2025-09-11','2025-09-11','2025-09-12','2025-09-13'],
    'date':['2025-09-11','2025-09-11','2025-09-12','2025-09-12'],
    'city':['서울', '안양', '서울', '안양'],
    'temp':[23, 22, 24, 22]},
    index=[1, 2, 3, 4]
)
print(df4)
df6 = df4.pivot(index='date', columns='city', values='temp')
print(df6)

# df7 = df4.drop(columns=['date', 'city'])  # drop specific columns
# print(df7)

# df8 = df4[df4.temp <= 23]
# df8 = df4.duplicated()
# print(df8)