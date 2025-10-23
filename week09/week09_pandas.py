import pandas as pd

uber = pd.read_csv("uber.csv")
# print(type(uber))
# print(uber.head(7))
# print(uber.info())
print(uber.describe())

# print(uber[uber["MILES*"] == 12204.7])  # describe
# print(uber[uber["MILES*"] == uber["MILES*"].max()])
# print(uber.tail())
uber = uber.drop(1155)
# print(uber.tail())
print(uber.describe())