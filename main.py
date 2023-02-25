from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel
from model import preprocess_data, make_prediction

description = """
This is Fast API Deployment of Heart Disease Prediction Model!

## Inputs

To begin input the following variables:

* **age** : Age in number
* **sex** : 'M' or 'F'
* **cigsPerDay**: How many cigarettes do you smoke per day?
* **BPMeds** : Are you currently on any Blood Pressure Meds? (Yes / No)
* **prevalentStroke** : Did you have a prevalent stroke? (Yes / No)
* **prevalentHyp** : Do you have prevalent hypertension? (Yes / No)
* **diabetes** : Do you have diabetes? (Yes / No)
* **totChol** : What is your total cholestrol level?
* **sysBP** : What is your systolic blood pressure?
* **heartRate** : What is your current heart rate?
* **glucose** : What is your current glucose level?

"""

class Info(BaseModel):
    age: int
    sex: Literal["M", "F"]
    cigsPerDay: float 
    BPMeds: Literal["Yes", "No"]
    prevalentStroke: Literal["Yes", "No"]
    prevalentHyp: Literal["Yes", "No"]
    diabetes: Literal["Yes", "No"]
    totChol: float
    sysBP: float
    BMI: float
    heartRate: float
    glucose: float

app = FastAPI(title='Heart Disease Predictor', description=description)

@app.get("/")
def index():
    return{"message": "Welcome to Heart Disease Predictor"}

@app.post("/predict")
def predict(data: Info):
    data = data.dict()
    prediction = make_prediction(data)
    if prediction == 1:
        print('You may have a risk of Coronary Heart Disease! Consult a doctor immediately!')
    else:
        print("You do not possess risk of Heart Disease! Continue to maintain a healthy lifestyle!")

    return prediction