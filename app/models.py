from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


# Create a base class for declarative models
Base = declarative_base()


# Define a SQLAlchemy model for the Currency table
class Currency(Base):
    """Class representing a currency."""
    # Table name
    __tablename__ = "currencies"

    # Columns in the table
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    code = Column(String, unique=True, index=True)
    rate = Column(Float)
    last_updated = Column(DateTime, default=datetime.utcnow)
