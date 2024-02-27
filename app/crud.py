from sqlalchemy.orm import Session
from app.models import Currency


def get_last_update(db: Session):
    return db.query(Currency.last_updated).order_by(Currency.last_updated.desc()).first()


def create_currency(db: Session, currency: Currency):
    db_currency = Currency(
        id=currency.id,
        name=currency.name,
        code=currency.code,
        rate=currency.rate['value'],  # Extract the 'value' from the rate dictionary
    )
    db.add(db_currency)
    db.commit()
    db.refresh(db_currency)
    return db_currency


def get_currency(db: Session, code: str):
    return db.query(Currency).filter(Currency.code == code).first()
