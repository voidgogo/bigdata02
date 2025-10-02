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

plt.figure(figsize=(8, 4))
sns.countplot(data=df, x="class", order=["First", "Second", "Third"])
plt.title("Passenger Count by Class", fontsize=14)
plt.xlabel("class")
plt.ylabel("Count")
# plt.tight_layout()
plt.show()
