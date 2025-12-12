import pandas as pd
import numpy as np

#pandas
df = pd.read_csv(r"C:\Users\Адм\Downloads\tested.csv")

print("Пропущенные значения")
print(df.isna().sum())

print("\nТипы данных")
print(df.dtypes)

n = 5
print(f"\nПервые {n} строк")
print(df.head(n))

print("\nСтатистика по возрасту")
print(df["Age"].describe())

rows, cols = df.shape
print("\nКоличество строк:", rows)
print("Количество столбцов:", cols)
print()

age_median = df["Age"].median()
df["Age"] = df["Age"].fillna(age_median)

df = df.dropna(subset=["Embarked"])

df = df.dropna()
df = df.iloc[:-20]

print("После очистки")
print(df.isna().sum())
print()

df.to_csv("tested2.csv", index=False)

#numpy
data = df

men = data[data["Sex"] == "male"]
women = data[data["Sex"] == "female"]

men_survival = np.mean(men["Survived"]) * 100
women_survival = np.mean(women["Survived"]) * 100

print("Процент выживших")
print("Мужчины:", men_survival)
print("Женщины:", women_survival)

print("\nСредний возраст")
print("Мужчины:", np.mean(men["Age"]))
print("Женщины:", np.mean(women["Age"]))
print()

survived = data[data["Survived"] == 1]
dead = data[data["Survived"] == 0]

print("Средний возраст")
print("Выжившие:", np.mean(survived["Age"]))
print("Погибшие:", np.mean(dead["Age"]))
print()

#старше 30, мужчины, 1 класс
group_a = data[(data["Age"] > 30) & (data["Sex"] == "male") & (data["Pclass"] == 1)]

#моложе 18 ИЛИ женщины, выжили
group_b = data[((data["Age"] < 18) | (data["Sex"] == "female")) & (data["Survived"] == 1)]

print("Фильтрация")
print("Группа A:", len(group_a))
print("Группа B:", len(group_b))

groupes = data.groupby(["Pclass", "Sex"])

print("\nСредний возраст")
print(groupes["Age"].mean())

print("\nДоля выживших")
print(groupes["Survived"].mean())

print("\nСредняя стоимость билета")
print(groupes["Fare"].mean())
