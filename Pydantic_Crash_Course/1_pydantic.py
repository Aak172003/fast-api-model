

# Inbuilt Validatior for nomal use case 
# If we want some , custom validator (we can use Field )
# If we want to add some more details with any key -> so we can use Annotated with Fields 

from email.policy import strict
from pydantic import EmailStr , Field
# from typing import Optional
from pydantic import BaseModel
from typing import List , Dict , Annotated


# This is pydantic model
# by default all keys are required in this pydantic model 
class Patient(BaseModel):
    # name should be upto 50 character 
    # name:str = Field(max_length=50)

    # Here add metadata with Annotate and Field
    name: Annotated[
        str,
        Field(
            max_length=50,
            title="Name of the patient",
            description="Give the name of the patient in less than 50 chars",
            examples=["Nitish", "Amit"]
        )
    ]    
    email:EmailStr
    age:int = Field(gt=0, lt=120)
    # weight:float = Field(gt=0)
    weight:Annotated[float , Field(gt=0, strict=True)]

    # to make boolean optional we can write like below  syntax , although if i make some key optional so i have to add some default value 
    # married:Optional[bool] = None
    married:Annotated[bool, Field(default=None, description="Is the patient married or not")]
    # married:bool

    # here perform 2 level type validation , 
    # if we use list -> it means we can check only allergies in list but inside user can add any type of value , so to perform 2 level type validation use from typing 
    # allergies:List[str] = Field(max_length=5)

    allergies:Annotated[List[str], Field(default=None , max_length=5)]
    contact_details:Dict[str , str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.married)
    print("data inserted into database ")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print("data updated into database ")


patient_info = {"name":"nitish","email":"abcdef@gmail.com", "age":'30' , "weight":75.2, "married":True, "allergies":["poolen", "dust"], "contact_details":{"email":"abc@gmail.com", "phone_no":"2345678"}}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)
update_patient_data(patient1)