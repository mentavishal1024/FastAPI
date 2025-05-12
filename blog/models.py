from sqlalchemy import Column, Integer, String
from .database import Base


class Blog(Base):
    __tablename__ = "blog"  # Define the name of the database table
    # Define the columns of the table
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    body = Column(String)

