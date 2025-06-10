import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd

model = joblib.load('iris_model.joblib')
scaler = joblib.load('iris_scaler.joblib')

app = FastAPI()

class IrisInput(BaseModel):
  sepal_length: float
  sepal_width: float
  petal_length: float
  petal_width: float

@app.post("/predict")
def predict(input: IrisInput):
  feature_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
  data = pd.DataFrame([[input.sepal_length, input.sepal_width, input.petal_length, input.petal_width]], columns=feature_names)
  data_scaled = scaler.transform(data)
  pred = model.predict(data_scaled)[0]
  species_map = {0: "setosa", 1: "versicolor", 2: "virginica"}
  return {"prediction": int(pred), "species": species_map[pred]}