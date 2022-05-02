from joblib import load
import numpy as np
from sklearn.metrics import mean_squared_error as mse

class Model:

    def __init__(self,columns):
        self.model = load("./modelo.joblib")

    def make_predictions(self, data):
        result = self.model.predict(data)
        return result

    def getR2(self, data, exp):
        print(data)
        print(exp)
        print("AAAAAA")
        predicted = self.model.predict(data)
        print("EEEEEE")
        print(exp)
        print(predicted)
        r2 = np.sqrt(mse(exp,predicted))
        print("zzzzzzz")
        return r2
