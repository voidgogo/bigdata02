import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("titanic")
# print(df.head())
# print(df.info())
# print(df.describe())

# plt.figure(figsize=(8, 4))
# sns.histplot(data=df, x="age", bins=16, kde=True)
# plt.title("Age Distribution of Passengers")
# plt.ylabel("Frequency")
# plt.xlabel("Age")
# # plt.tight_layout()
# plt.show()

# plt.figure(figsize=(8, 4))
# sns.countplot(data=df, x="survived")
# plt.title("Survivors vs Non-survivors", fontsize=14)
# plt.xlabel("Survived (0: No, 1: Yes)")
# plt.ylabel("Count")
# # plt.tight_layout()
# plt.show()

# plt.figure(figsize=(8, 4))
# sns.countplot(data=df, x="class", order=["First", "Second", "Third"])
# plt.title("Passenger Count by Class", fontsize=14)
# plt.xlabel("Class")
# plt.ylabel("Count")
# # plt.tight_layout()
# plt.show()

# plt.figure(figsize=(8, 4))
# sns.countplot(data=df, x="sex", hue="survived")
# plt.legend(loc="upper right", title="Survived", labels=["No", "Yes"])
# plt.title("Survival Status by Gender", fontsize=14)
# plt.xlabel("Sex")
# plt.ylabel("Count")
# plt.tight_layout()
# plt.show()

# plt.figure(figsize=(8, 4))
# sns.boxplot(data=df, x="class", y="fare", order=['First', 'Second', 'Third'])
# plt.title("Fare Distribution by Class", fontsize=14)
# plt.xlabel("Class")
# plt.ylabel("Fare")
# plt.show()

# plt.figure(figsize=(8, 4))
# sns.violinplot(data=df, x="survived", y="age")
# plt.title("Age Distribution by Survival Status", fontsize=14)
# plt.xlabel("Survived (0: No, 1: Yes)")
# plt.ylabel("Age")
# plt.show()

plt.figure(figsize=(8, 4))
sns.catplot(
    data=df, x="class", hue="survived", col="sex",
    kind="count", order=["First", "Second", "Third"])
plt.show()