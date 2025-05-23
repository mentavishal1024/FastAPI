from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn


app = FastAPI()

@app.get("/blog") #app is decorator, ("/") is the path, get is the operation 
# path operation function
def index(limit, published:bool): #Query parameters 
    if published:
        return {"data":f"{limit} published blogs from the db"} 
    else:
        return {"data":f"{limit} blogs from the db"}
    

@app.get("/blog/unpublished") #app is decorator, ("/blog/unpublished") is the path, get is the operation
def unpublished():
    return {"data":"unpublished blogs"}

@app.get("/blog/{id}") #app is decorator, ("/blog/{id}") is the path parameter giving dynamically, get is the operation
def show(id:int):
    return {"data": id} #id is the path parameter giving dynamically

@app.get("/blog/{id}/comments") #app is decorator, ("/blog/{id}/comments") is the path parameter giving dynamically, get is the operation
def comments(id):
    return {"data":{"1", "2"}}

class Blog(BaseModel):  # Define a Pydantic model for data validation
    title: str  # Title of the blog (required field)
    body: str  # Body/content of the blog (required field)
    published: Optional[bool]  # Optional field to indicate if the blog is published

@app.post("/blog")
def create_blog(request:Blog):
    return {'data':f"blog is created with title as {request.title}"} #request is the request body


# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1",port = 9000)