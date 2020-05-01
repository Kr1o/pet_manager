import os

from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

base_path = os.path.abspath('database.db')
engine = create_engine(f'sqlite:///{base_path}', echo=True, encoding='utf-8')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

pet_owner = Table('pet_owner', Base.metadata,
                  Column('user_id', Integer, ForeignKey('user.id')),
                  Column('pet_id', Integer, ForeignKey('pet.id'))
                  )


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    tg_user_id = Column(String)
    tg_user_first_name = Column(String)
    pets = relationship('Pet', secondary=pet_owner)

    def __repr__(self):
        return "Имя: '%s', Телеграм ID: '%s'" % (self.tg_user_first_name, self.tg_user_id)


class Pet(Base):
    __tablename__ = 'pet'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    #    birth_date = Column(Date)
    #    feed_weight = Column(Integer)
    #    feed_in_day = Column(Integer)
    #    vaccination = Column(Boolean)
    #    tick_protect = Column(Boolean)
    #    vaccination_date = Column(Date)
    #    tick_protect_date = Column(Date)

    def __repr__(self):
        return "Имя: '%s', Дата рождения: '%s'" % (self.name, self.name)
