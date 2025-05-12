from pydantic import BaseModel

class Blog(BaseModel):  # Define a Pydantic model for data validation
    title:str
    body:str 
