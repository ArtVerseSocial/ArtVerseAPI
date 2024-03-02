from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SportList(Base):
    __tablename__ = "sport_list"

    id = Column(Integer, primary_key=True)
    name = Column(String)

class SportUser(Base):
    __tablename__ = "sport_user"

    id = Column(Integer, primary_key=True)
    sport_id = Column(Integer)
    user_id = Column(Integer)