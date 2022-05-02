import numpy as np
import pandas as pd
from joblib import dump, load
from fastapi import FastAPI

from DataModel2 import *
from DataModel import *
from sklearn.metrics import mean_squared_error as mse


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/predict")
def make_predictions(dataModel: DataModel):
    df = pd.DataFrame(dataModel.dict(), index=[0], columns=dataModel.dict().keys())
    df.columns = dataModel.columns()
    model = load("assets/modelo.joblib")
    result = model.predict(df)
    return result.tolist()

@app.post("/r2")
def make_r2(dataModel: DataModel, dataModel2: DataModel2):
    df2 = pd.DataFrame(dataModel2.dict(), index=[0], columns=dataModel2.dict().keys())
    df2.columns = dataModel2.columns()
    df = pd.DataFrame(dataModel.dict(), index=[0], columns=dataModel.dict().keys())
    df.columns = dataModel.columns()
    model = load("assets/modelo.joblib")
    result = model.predict(df)

    print(model.predict(df))

    return np.sqrt(mse(df2, model.predict(df)))