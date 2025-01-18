# app.py
from fastapi import FastAPI
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from pydantic import BaseModel
import joblib
import redis

app = FastAPI()

# Load the pre-trained model
model = joblib.load("iris_model.joblib")

#r = redis.Redis(host="localhost", port=6379, db=0)

# Define the input data model
class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Create a prediction endpoint
@app.post("/predict")
def predict_iris_species(data: IrisData):
    # Convert the input data to a numpy array
    input_data = [[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]]

    # Make a prediction using the loaded model
    prediction = model.predict(input_data)[0]
    
    # save to redis key-value pair database for caching
    #r.set(set(input_data),prediction)

    # Return the predicted species
    return {"prediction": str(prediction)}

# Create a health check endpoint
@app.get("/health")
def health():
    return {"status": "ok"}
