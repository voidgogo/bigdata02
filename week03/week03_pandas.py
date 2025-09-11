import pandas as pd

df4 = pd.DataFrame({
    '날짜':['2025-09-11','2025-09-11','2025-09-12','2025-09-12'],
    '도시':['서울', '안양', '서울', '안양'],
    '온도':[23, 22, 24, 26]},
    index=[1, 2, 3, 4]
)
print(df4)
df5 = df4.pivot(index='날짜', columns='도시', values='온도')
print(df5)