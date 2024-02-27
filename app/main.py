from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import crud, database, exchange
from pydantic import BaseModel


class ConvertRequest(BaseModel):
    source: str
    target: str
    amount: float


app = FastAPI()


# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/update_exchange_rates")
async def update_exchange_rates(db: Session = Depends(get_db)):
    exchange.update_exchange_rates(db)
    return {"message": "Exchange rates updated successfully"}


@app.get("/last_update")
async def last_update(db: Session = Depends(get_db)):
    last_update_time = crud.get_last_update(db)
    return {last_update_time}


@app.post("/convert")
async def convert_currency(
    request_data: ConvertRequest, db: Session = Depends(get_db)
):
    result = exchange.convert_currency(db, request_data.source, request_data.target, request_data.amount)
    return {"result": result}
