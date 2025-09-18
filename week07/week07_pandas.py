import seaborn as sns
from matplotlib import pyplot as plt

titanic = sns.load_dataset("titanic")
plt.figure(figsize = (15,12))

plt.subplot(2, 3, 1)
sns.boxplot(data=titanic, x="survived", y="age")
plt.title("Age Distribution by Survival Status")
plt.xlabel("Survived (0: No, 1: Yes)")
plt.ylabel("Age")

plt.subplot(2, 3, 2)
sns.boxplot(data=titanic, x="sex", y="age")
plt.title("Age Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Age")

plt.subplot(2, 3, 3)
sns.boxplot(data=titanic, x="class", y="fare")
plt.title("Fare Distribution by Class")
plt.xlabel("Passenger Class")
plt.ylabel("Fare")

plt.subplot(2, 3, 4)
sns.boxplot(data=titanic, x="survived", y="fare")
plt.title("Fare Distribution by Survival Status")
plt.xlabel("Survived (0: No, 1: Yes)")
plt.ylabel("Fare")

plt.subplot(2, 3, 5)
sns.boxplot(data=titanic, x="sex", y="age", hue="survived", palette="Set2")
plt.title("Age Distribution by Survival Status")
plt.title("Age by Gender and Survival")
plt.xlabel("Gender")
plt.ylabel("Age")
plt.legend(title="Survived", labels=["No", "Yes"])

plt.show()