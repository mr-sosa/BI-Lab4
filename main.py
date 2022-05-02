from ctypes import Array
from typing import Optional
from typing import List
from unittest import result
from PredictionModel import Model
from fastapi import FastAPI
from joblib import load
import pandas as pd


#import DataModel
from pydantic import BaseModel

from pydantic import BaseModel

class DataModel(BaseModel):
# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    adult_mortality: float
    infant_deaths: float
    alcohol: float
    percentage_expenditure: float
    hepatitis_B: float
    measles: float
    bmi: float
    under_five_deaths: float
    polio: float
    total_expenditure: float
    diphtheria: float
    hiv_aids: float
    gdp: float
    population: float
    thinness_10_19_years: float
    thinness_5_9_years: float
    income_composition_of_resources	: float
    schooling: float

#Esta función retorna los nombres de las columnas correspondientes con el modelo esxportado en joblib.
    def columns(self):
        return ["Adult Mortality", "infant deaths", "Alcohol","percentage expenditure","Hepatitis B", "Measles", "BMI",
                "under-five deaths", "Polio", "Total expenditure", "Diphtheria", "HIV/AIDS", "DGP", "Population",
                "thinness 10-19 years", "thinness 5-9 years", "Income composition of resources", "Schooling"]


class nModel(BaseModel):
    predictor: List[DataModel]
    expected: List[float]



app = FastAPI()


@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
def make_predictions(dataModel: DataModel):
    df = pd.DataFrame(dataModel.dict(), columns=dataModel.dict().keys(), index=[0])
    df.columns = dataModel.columns()
    model = Model(df.columns)
    result = model.make_predictions(df)
    return result.tolist()

@app.post("/r")
def r(dat: nModel):
    df = pd.DataFrame()
    for x in range(len(dat.predictor)):
        df = pd.concat([df, pd.DataFrame(dat.predictor[x])], keys=dat.predictor[x].dict().keys())

    print("1")
    df.columns = dat.predictor[0].columns()
    print("2")
    model = Model(df.columns)
    print("3")
    expected = dat.expected
    print("4")
    result = model.getR2(df, expected)
    print("5")
    return result.tolist()

