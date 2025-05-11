from fastapi import FastAPI

app = FastAPI()

@app.get("/") #app is decorator, ("/") is the path, get is the operation 
# path operation function
def index():
    return {"data":"blog list"} 

@app.get("/blog/{id}") #app is decorator, ("/blog/{id}") is the path parameter giving dynamically, get is the operation
def show(id:int):
    return {"data": id} #id is the path parameter giving dynamically

@app.get("/blog/{id}/comments") #app is decorator, ("/blog/{id}/comments") is the path parameter giving dynamically, get is the operation
def comments(id):
    return {"data":{"1", "2"}}



