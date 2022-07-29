import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def predictor():
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def predictor():
    credit_card_data = pd.read_csv('creditcard.csv')

    fraud = credit_card_data[credit_card_data['Class'] == 1]
    legit = credit_card_data[credit_card_data["Class"]==0]
    legit_sample = legit.sample(n=399)
    new_dataset = pd.concat([legit_sample, fraud], axis=0)

    X = new_dataset.drop(columns='Class', axis=1)
    Y = new_dataset['Class']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    return model

