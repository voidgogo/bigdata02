import pandas as pd

uber = pd.read_csv("uber.csv")
uber['START_DATE*'] = pd.to_datetime(uber['START_DATE*'], errors='coerce')
uber['END_DATE*'] = pd.to_datetime(uber['END_DATE*'], errors='coerce')
uber = uber.sort_values(['START_DATE*', 'END_DATE*'])
uber = uber.drop(1155)
uber['DURATION*'] = (uber['END_DATE*'] - uber['START_DATE*']).dt.total_seconds() / 60
# print(uber['CATEGORY*'].value_counts())
# print(uber.groupby(['CATEGORY*', 'PURPOSE*']))
print(uber.groupby(['CATEGORY*', 'PURPOSE*'])[['MILES*','DURATION*']].agg(['mean', 'median', 'count']))
print(uber[uber['PURPOSE*'] == 'Airport/Travel'][['MILES*', 'DURATION*']])