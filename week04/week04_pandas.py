import numpy as np
import pandas as pd
import seaborn as sns

def square(x):
    return x ** 2
def cube(x):
    return x ** 3

mpg = sns.load_dataset("mpg")
df = pd.DataFrame([
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
], columns=['A', 'B', 'C'], index=[1, 2, 3])
print(df)
print(df.apply(square))
print(df.apply(cube))