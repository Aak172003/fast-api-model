# A computed field is a field in a Pydantic model whose value is automatically derived from other fields rather than being provided directly by the user.



from pydantic import BaseModel , EmailStr, computed_field
from typing import List , Dict

class Patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    weight:float
    height:float
    allergies:List[str]
    contact_details:Dict[str , str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi

def update_patient_details(patient):
    print(patient.age)
    print(patient.name)
    print("Bmi ----- ", patient.bmi)
    print("data updated into database ")


patient_info = {"name":"nitish","email":"abcdef@gmail.com", "age":'30' , "weight":75.2, "height":1.72, "married":True, "allergies":["poolen", "dust"], "contact_details":{"email":"abc@gmail.com", "phone_no":"2345678"}}


patient1 = Patient(**patient_info)


update_patient_details(patient1)