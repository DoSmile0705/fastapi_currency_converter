from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import crud, models
import httpx

url = "https://api.currencyapi.com/v3/latest"
headers = {
    'apikey': "cur_live_V7mTQy7pPdfIuUpqFOFEkXh7GkwKlE2svf2MvOZc"
}
apikey = "cur_live_V7mTQy7pPdfIuUpqFOFEkXh7GkwKlE2svf2MvOZc"


def update_exchange_rates(db: Session):
    # Call external API to get exchange rates
    response = httpx.get("https://api.currencyapi.com/v3/latest?apikey=" + apikey)
    print(response)
    data = response.json()
    if response.status_code != 200 or "data" not in data:
        raise HTTPException(status_code=500, detail="Failed to fetch exchange rates")

    # Update or create currencies in the database
    for code, rate in data["data"].items():
        currency = crud.get_currency(db, code)
        if currency:
            currency.rate = rate
        else:
            crud.create_currency(db, models.Currency(id=code, code=code, rate=rate))

    # Update the last update time
    # last_update_time = crud.get_last_update(db)


def convert_currency(db: Session, source: str, target: str, amount: float):
    source_currency = crud.get_currency(db, source)
    target_currency = crud.get_currency(db, target)

    if not source_currency or not target_currency:
        raise HTTPException(status_code=404, detail="Currency not found")

    converted_amount = (amount / source_currency.rate) * target_currency.rate
    return converted_amount
