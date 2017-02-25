# -*- coding: utf-8 -*-
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import relationship

from models import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String, nullable=True, unique=True)
    email = Column(String, nullable=False)
    real_name = Column(String, nullable=False)

    posts = relationship('Quote', back_populates='poster')
    quotes = relationship('Quote', back_populates='quoted')
    ratings = relationship('QuoteRating', back_poulates='user')
