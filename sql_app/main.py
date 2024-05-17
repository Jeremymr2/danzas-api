from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/hello")
async def root():
    return {"message": "Hello World"}

@app.get("/", response_model=List[schemas.Expresion])
def read_expresiones(db: Session = Depends(get_db)):
    expresiones = crud.get_expresiones(db)
    return expresiones