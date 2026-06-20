#Write a program to develop the Naive Bayes classifier on Titanic dataset.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix

df = pd.read_csv("Titanic-Dataset.csv")
df = df[['Survived','Pclass','Age','SibSp','Parch','Fare','Embarked']]

df[['Age','Fare']] = SimpleImputer(strategy='median').fit_transform(df[['Age','Fare']])
df['Embarked'] = LabelEncoder().fit_transform(df['Embarked'].fillna(df['Embarked'].mode()[0]))

X = df.drop('Survived', axis=1)
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Accuracy:", model.score(X_test, y_test))