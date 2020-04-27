import os

from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base_path = os.path.abspath('database.db')
engine = create_engine(f'sqlite:///{base_path}', echo=True, encoding='utf-8')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Pet(Base):
    __tablename__ = 'pet'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_date = Column(Date)
    feed_weight = Column(Integer)
    feed_in_day = Column(Integer)
    vaccination = Column(Boolean)
    tick_protect = Column(Boolean)
    vaccination_date = Column(Date)
    tick_protect_date = Column(Date)

    def __repr__(self):
        return "Имя: '%s', Дата рождения: '%s'" % (self.name, self.birth_date)
