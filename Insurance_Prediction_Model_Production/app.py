from model.predict import predict_output, MODEL_VERSION, model
from schema.user_input import UserInput
from fastapi.responses import JSONResponse

from fastapi import FastAPI

app = FastAPI()


# This is huma redable
@app.get("/")
def home():
    return {'message':"Insurance Premium Predction"}

# This is machine redable
# This is health Check API
@app.get("/health")
def health_check():
    return {
        'status':"OK",
        "version":MODEL_VERSION,
        'model_loaded': model is not None
    }

@app.post('/predict')
def predict_premium(data: UserInput):
    # creating dataframe 
    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    prediction = predict_output(user_input)
    print("prediction value : ", prediction)
    
    return JSONResponse(status_code=200, content={'predicted_category': prediction})