import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from . import connection as con
import pickle 
import os

def run():
      rows = con.db_val(2)
      main_data = pd.DataFrame(rows)

      # legit - 28337 , fraud - 93
      legit = main_data[main_data[30] == 0] 
      fraud = main_data[main_data[30] == 1]
      perc_legit = (legit/main_data)*100
      perc_fraud = (fraud/main_data)*100

      legitV = legit.sample(n=93) 
      data = pd.concat([legitV,fraud] , axis=0)
      X = data.drop(columns=30 , axis=1)
      Y = data[30]
      Z = data[29]

      model_path = os.path.join(os.getcwd(), "model_pickel")
      with open(model_path,"rb") as f:
          model=pickle.load(f)
      #training model and fitting data 
      #with open("model_pickel","rb") as f:
      #      model=pickle.load(f)

      #model fit and ran for predicting
      rows = X.values.tolist()
      cash = Z.values.tolist()
      predict_data = []
      for row in rows:
            x_val=pd.DataFrame(row)
            vals = x_val.values.transpose()
            x_val = pd.DataFrame(vals)
      #       print(type(x_val),vals.shape)
            X_vals_prediction = model.predict(x_val)
            if X_vals_prediction == 1:
                  c='fraud'
            else:
                  c='legit'
            predict_data.append(c)
            
            X_vals_pred = pd.DataFrame(predict_data)
      return predict_data,cash,perc_fraud,perc_legit
      # print(predict_data)
if __name__ == "__main__":
      run()
      #   X_test_pred = np.append(X_test_prediction)