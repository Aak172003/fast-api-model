# We can combine multiple fields and validate them together in Pydantic . 

from pydantic import BaseModel , EmailStr , model_validator
from typing import List , Dict

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    allergies:List[str]
    contact_details:Dict[str , str]

    # get value after type cohesion
    @model_validator(mode="after")
    def validate_emergency_contact(cls , model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patients older than 60 must have an emergency contact")
        else:
            return model


def update_patient_details(patient):
    print(patient.age)
    print(patient.name)
    print(patient.allergies)
    print("data updated into database ")


patient_info = {"name":"nitish","email":"abs@icici.com", "age":"65" , "weight":75.2, 
"married":True, "allergies":["poolen", "dust"], "contact_details":{"phone_no":"2345678", "emergency":"2345678"}}


patient1 = Patient(**patient_info)

update_patient_details(patient1)

