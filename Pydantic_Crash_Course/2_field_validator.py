# Field-validator can be used for data validator 
# and we can use for any kind of transformation 
from pydantic import field_validator
from pydantic import EmailStr
from pydantic import BaseModel

class Patient(BaseModel):
    name:str 
    email:EmailStr
    age:int

    # Here setup email validator 
    @field_validator('email')
    @classmethod
    def email_validator(cls , value):
        valid_domains = ['hdfc.com', "icici.com"]
        domain_name =  value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        return value

    @field_validator('name')
    @classmethod
    def transfor_name(cls , value):
        return value.title()


    # bydeafult mode set to after  -> it means get value after cohesion    
    @field_validator('age', mode="after")
    @classmethod
    def validate_age(cls , value):
        if 0 < value < 100:
            return value
        else:
            return ValueError('Age should be in between 0 to 100')

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print("data inserted into database ")

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)

    print("data updated into database ")


patient_info = {"name":"nitish","email":"abs@icici.com", "age":"30"}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)
# update_patient_data(patient1)