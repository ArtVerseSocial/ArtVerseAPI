from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SportList(Base):
    __tablename__ = "sport_list"

    id = Column(Integer, primary_key=True)
    name = Column(String)