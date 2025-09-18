import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('savant_data.csv')
# print(df.info())
# print(df['player_name'])
df_new = df[['player_id', 'player_name', 'total_pitches', 'velocity', 'hrs', 'so', 'bb']]
# print(df_new.info())
# print(df_new.head())
# print(df_new.query('player_name == "Ohtani, Shohei"'))
# print(df_new.query('player_id == 660271'))
# print(df_new.sort_values('velocity', ascending=False))
# print(df_new.sort_values('so', ascending=False))

# print(df_new.query('player_name == "Ohtani, Shohei"'))
# print(df_new.describe())

# print(len(df_new[df_new['total_pitches'] > 1000]))
print(len(df_new.query('total_pitches > 1000')))

# plt.figure(figsize = (10, 5))
# plt.boxplot(df_new['total_pitches'])
# plt.show()


# plt.title('Ohtani, Shohei', fontsize=20, fontweight='bold')
# plt.xlabel('player_id', fontsize=15)
# plt.ylabel('total_pitches', fontsize=15)
# # plt.xticks(fontsize=15)
# # plt.yticks(fontsize=15)
# plt.show()
