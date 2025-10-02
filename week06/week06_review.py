import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset("titanic")
# print(df.groupby("sex")['survived'].mean())
print(df.groupby(['sex', 'class'])['survived'].agg(['mean', 'count']))

# plt.figure(figsize=(8, 4))
# sns.countplot(data=df, x="sex", hue="survived")
# plt.legend(loc="upper right", title="Survived", labels=["No", "Yes"])
# plt.title("Survival Status by Gender", fontsize=14)
# plt.xlabel("Sex")
# plt.ylabel("Count")
# plt.tight_layout()
# plt.show()
