from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Currency(Base):
    """Class representing a currency."""
    __tablename__ = "currencies"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    code = Column(String, unique=True, index=True)
    rate = Column(Float)
    last_updated = Column(DateTime, default=datetime.utcnow)
