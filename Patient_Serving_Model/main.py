from typing import Literal
import json
# This is used to return json response when api completed 
from fastapi.responses import JSONResponse

from fastapi import FastAPI , Path , HTTPException, Query
from pydantic import BaseModel ,Field , computed_field

# Annoted is used to add desciption 
from typing import Annotated

# This is computed fileds in pydatic through which we can compue any value which we will not get from client end

# with the help of path we can enhance redablity of any endpoint 
# HTTPException -> HTTPException is a special built-in exception n FastAPI used to return custom HTTP error response when something goes wrong in HTTP API 
# Query -> is a utility function provided by FastAPI to declare , validate and document query parameter , same work like parameter 
app = FastAPI()


class Patient(BaseModel):
    id: Annotated[str , Field(..., description="Id of the Patient", examples=["P001"])]
    name: Annotated[str, Field(..., description="Name of the patient")]
    city: Annotated[str, Field(..., description="City where the patient is living")]
    age:  Annotated[int, Field(..., gt=0 , lt=120 ,  description="Age of the patient")]
    gender: Annotated[Literal["male", "female", "others"], Field(..., description="Gender of the patient")]
    height:  Annotated[float, Field(..., gt=0  ,  description="Height of the patient in mtrs")]
    weight: Annotated[float, Field(..., gt=0 ,  description="Weight of the patient in kgs")]

    # phle verdit trigger horha hai then bmi trigger ho rha hai 
    @computed_field
    @property
    def bmi(self)-> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

    @computed_field
    @property
    def verdit(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"   
        elif self.bmi < 30:
            return "Normal" 
        else:
            return "Obese" 

def load_data():
    with open('patients.json', "r") as f:
        data = json.load(f)
        print("this is data : : : : ", data)
    return data


def save_data(data):
    with open('patients.json', "w") as f:
        json.dump(data , f)

@app.get("/")
def hello():
    return {'message':"Patient management system api"}


@app.get("/about")
def about():
    return{ 'message':"a fully functional API to manage your patient records"}


@app.get("/view")
def view():
    data = load_data()
    return data 


@app.get("/patient/{patient_id}")
def view_patient(patient_id:str=Path(..., description="Id of the Patient ", example="P001")):
    # load all the patient data 
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    # return {'error':"Patient not found"}
    raise HTTPException(status_code = 404 , detail="Patient not found")


# so here ... means it is required , and rest not required means optional 
@app.get("/sort")
def sort_patient(sort_by: str = Query(..., description="Sort by height, weight or bmi"),order: str = Query("asc", description="Sort in asc or desc order")):
    valid_fields = ["height", "weight", "bmi"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f"Invalid field. Select from {valid_fields}")

    valid_orders = ["asc", "desc"]
    if order not in valid_orders:
        raise HTTPException(status_code=400,detail=f"Invalid order. Select from {valid_orders}")

    data = load_data()
    # get sorted data based on sort_by and sort_order
    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=(order == "desc")
    )

    return sorted_data


@app.post("/create")
def create_patient(patient:Patient):
    # load existing data
    data = load_data()

    # check if the patient already exist or not 
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient Already Exist")

    # New patient add to database     
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save into the json file 
    save_data(data)

    # return successfull response 
    return JSONResponse(status_code = 201 , content={"message":"patient created successfully"})


    

