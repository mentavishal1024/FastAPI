from fastapi import FastAPI, Depends
from . import schema,models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session


models.Base.metadata.create_all(engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog")
def creat(request:schema.Blog,db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog")
def all(db:Session = Depends(get_db)):
    blog = db.query(models.Blog).all()
    return blog

@app.get("/blog/{id}")
def get_blog_by_id(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        return blog
    else:
        return {"error":"Sorry Blog not found"}

