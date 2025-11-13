import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

usc = pd.read_csv('us_corona19.csv')
# print(usc.info())
# print(usc.describe())
# print(usc['Admin2'])
print(usc[usc['Admin2'].isna()])

# print(usc.dropna())

# new_usc = usc.fillna('Daelim')
# print(new_usc.query('Admin2 == "Daelim"'))