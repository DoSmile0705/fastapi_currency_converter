import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('POSTGRES_USER')
databasename = os.getenv('POSTGRES_DB')
password = os.getenv('POSTGRES_PASSWORD')

# Database connection URL
DATABASE_URL = f"postgresql://{username}:{password}@localhost/{databasename}"

# Create a SQLAlchemy engine for the database connection
engine = create_engine(DATABASE_URL)

# Create a sessionmaker for handling database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()
