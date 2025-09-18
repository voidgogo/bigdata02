import numpy as np
import pandas as pd
import seaborn as sns

mpg = sns.load_dataset("mpg")
df = pd.DataFrame([
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
], columns=['A', 'B', 'C'], index=[1, 2, 3])
print(df)
print(df.apply(lambda x : x*x))
print(df.apply(lambda z : z**3))