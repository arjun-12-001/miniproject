import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import os

csv_path = os.path.join(os.getcwd(), "creditcard.csv")
credit_card_data = pd.read_csv(csv_path)

fraud = credit_card_data[credit_card_data['Class'] == 1]
print(len(fraud))
legit = credit_card_data[credit_card_data["Class"]==0]
print(len(legit))
legit_sample = legit.sample(n=len(fraud))
new_dataset = pd.concat([legit_sample, fraud], axis=0)
print(new_dataset)

X = new_dataset.drop(columns='Class', axis=1)
Y = new_dataset['Class']
print(len(new_dataset))
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)
#Y_train_val=Y_train.sample(n=len(Y_test))l


model = LogisticRegression()
model.fit(X_train, Y_train)
val_predictions = model.predict(X_test)
print(100*(accuracy_score(Y_test, val_predictions)))


#with open("model_pickel","wb") as f:
#    pickle.dump(model,f)

