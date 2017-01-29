from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, REAL
from sqlalchemy import create_engine
from settings import DB_NAME

Base = declarative_base()


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    balance = Column(REAL, default=0)

    def __str__(self):
        return '{} {}'.format(id, self.username)

    def __repr__(self):
        return self.__str__()


class BannedClient(Base):
    __tablename__ = 'banned_client'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    ban_time = Column(REAL)

engine = create_engine(DB_NAME)
Base.metadata.create_all(engine)
