

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# loading the dataset
iris = load_iris()
X = iris.data   # characteristics
y = iris.target # flowers

# data division
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# creating model Gaussian Naive Bayes
model = GaussianNB()

# training the model
model.fit(x_train, y_train)

# making predictions
y_pred = model.predict(x_test)

# testing the model
accuracy = accuracy_score(y_test, y_pred) * 100
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Report:\n{report}")

