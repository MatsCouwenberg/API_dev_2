from sqlalchemy import Column, Integer, String
from database import Base

class Driver(Base):
    __tablename__ = "drivers"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, index=True)
    name = Column(String, index=True)
    nationality = Column(String, index=True)

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    country = Column(String, index=True)
