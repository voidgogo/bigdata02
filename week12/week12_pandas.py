import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

wh = pd.read_csv('wh.csv')
# print(wh.info())
# print(wh.head())
# print(wh.describe())
# 파운드 (1 == 453.592g), 인치 (1 == 2.54cm)
print(wh.query('Weight > 390'))
print(wh[wh['Weight'] > 390])
# sns.scatterplot(x='Weight', y='Height', data=wh)
# plt.show()
