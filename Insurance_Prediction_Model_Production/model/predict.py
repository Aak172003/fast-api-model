import pickle
from pathlib import Path

import pandas as pd


# First import the ml model
MODEL_PATH = Path(__file__).resolve().parent / "model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
 
MODEL_VERSION = "1.0.0"

# get output classes name 
# as we have high , medium and low 
class_labels = model.classes_.tolist() 

def predict_output(user_input: dict):

    # --------------------------------  here just returning output data 

    # input_df = pd.DataFrame([user_input])

    # output = model.predict(input_df)[0]
    # return output


    # --------------------------------  This is the way how we can get more info like confidence score  if we use random forest 
    df = pd.DataFrame([user_input])

    # Predict the class 
    predicted_class = model.predict(df)[0]

    # Get Probablities for all classes 
    probablities = model.predict_proba(df)[0]
    confidence = max(probablities)

    # create mapping
    class_probs = dict(zip(class_labels, map(lambda p: round(p,4), probablities)))
    return {
        'predicted_category':predicted_class,
        'confidence':round(confidence, 4),
        'class_probablities':class_probs
    }
