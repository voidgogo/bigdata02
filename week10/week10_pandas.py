import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

korean = pd.read_csv('korean.csv')
# print(korean['Age'].value_counts().sort_values(ascending=False))
print(pd.qcut(korean['Age'], q=8).reset_index().groupby('Age').size())