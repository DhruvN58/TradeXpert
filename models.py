# models.py
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Define the Base
Base = declarative_base()

# Set up your database URL (for example, SQLite, Postgres, etc.)
DATABASE_URL = "sqlite:///./test.db"  # SQLite database for this example

# Create the engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # For SQLite

# Create the sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define your models (TradeDB and User)
class TradeDB(Base):
    __tablename__ = "trades"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    symbol = Column(String, index=True)
    action = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

# Create the tables in the database
Base.metadata.create_all(bind=engine)
