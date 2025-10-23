import pandas as pd

uber = pd.read_csv("uber.csv")
# uber['START_DATE*'] = pd.to_datetime(uber['START_DATE*'])
# print(uber)
uber['START_DATE*'] = pd.to_datetime(uber['START_DATE*'], errors='coerce')
uber['END_DATE*'] = pd.to_datetime(uber['END_DATE*'], errors='coerce')
uber = uber.sort_values(['START_DATE*', 'END_DATE*'])
# print(uber.info())
# print(uber['START_DATE*'])
# print(uber['START_DATE*'].unique())
uber = uber.drop(1155)
# print(uber['END_DATE*'].unique())
# print(uber[uber['MILES*'] == uber['MILES*'].min()])
# print(uber['PURPOSE*'].value_counts())
# print(uber['PURPOSE*'].isna().sum())

# uber['DURATION*'] = (uber['END_DATE*'] - uber['START_DATE*'])
uber['DURATION*'] = (uber['END_DATE*'] - uber['START_DATE*']).dt.total_seconds() / 60
# print(uber['DURATION*'])
print(uber.info())