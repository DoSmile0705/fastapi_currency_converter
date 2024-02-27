from sqlalchemy.orm import Session
from app.models import Currency


def get_last_update(db: Session):
    """Get the timestamp of the last currency update from the database."""
    return db.query(Currency.last_updated).order_by(Currency.last_updated.desc()).first()


def create_currency(db: Session, currency: Currency):
    """
    Create a new currency entry in the database.

    :param db: Database session
    :param currency: Currency model containing information about the currency
    :return: The created currency entry
    """
    # Extract the 'value' from the rate dictionary
    db_currency = Currency(
        id=currency.id,
        name=currency.name,
        code=currency.code,
        rate=currency.rate['value'],
    )
    db.add(db_currency)
    db.commit()
    db.refresh(db_currency)
    return db_currency


def get_currency(db: Session, code: str):
    """
    Retrieve a currency entry from the database based on its code.

    :param db: Database session
    :param code: Currency code
    :return: The currency entry if found, otherwise None
    """
    return db.query(Currency).filter(Currency.code == code).first()
