from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from environs import Env


env = Env()

env.read_env('config.env')

USER_BASE = env.str('USER')
PASSWORD = env.str('PASSWORD')
HOST = env.str('HOST')
PORT = env.int('PORT')
DATA_BASE = env.str('DATA_BASE')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    date = Column(DateTime)
    file_id = Column(String)
    file_path = Column(String)

class Product(Base):
    __tablename__ = 'basket'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    product_id = Column(Integer)
    name = Column(String)
    count = Column(Integer)
    price = Column(Integer)

engine = create_engine(f'postgresql+psycopg2://{USER_BASE}:{PASSWORD}@{HOST}:{PORT}/{DATA_BASE}')

Session = sessionmaker(bind=engine)

session = Session()

Base.metadata.create_all(engine)
