from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from environs import Env
from datetime import datetime

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

engine = create_engine(f'postgresql+psycopg2://{USER_BASE}:{PASSWORD}@{HOST}:{PORT}/{DATA_BASE}')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

user = User(
    user_id=12342,
    user_name='craster',
    date=datetime.now(),
    file_id="djfhsdjkfjdshgf",
    file_path='sdfds'
)
session.add(user)
session.commit()