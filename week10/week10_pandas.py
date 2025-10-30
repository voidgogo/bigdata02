import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

s1 = pd.Series([0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0])
# print(s1)
sc1 = s1.cumsum()  # cumulative sum
# print(sc1)
# print(s1.mul(sc1))  # multiply
# print(s1.mul(sc1).diff())  # difference
# print(s1.mul(sc1).diff().where(lambda n: n>0))  # where (if)
# print(s1.mul(sc1).diff().where(lambda n: n > 0).ffill())  # front fill
print(s1.mul(sc1).diff().where(lambda n: n > 0).ffill().add(sc1, fill_value=0))  # add 0